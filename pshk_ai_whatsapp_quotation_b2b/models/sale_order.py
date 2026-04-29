from odoo import models, fields, api
from odoo.tools import html2plaintext
from odoo.exceptions import UserError
import json
import difflib

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    # AI Tools

    @api.model
    def _ai_product_search(self, product_name):
        # Search for products based on the product name to get the product ID
        products = self.env['product.product'].search([]).read(['display_name'])
        product_list = []
        for product in products:
            product_list.append(product['display_name'])

        products = difflib.get_close_matches(product_name, product_list, n=3, cutoff=0.4)
        products = [self.env['product.product'].search([('display_name', '=', product)], limit=1)._ai_read(['display_name'], None) for product in products]
        
        response = "⚠️ Never share the info below with the user. It can only by used by you when creating a quotation with the quotation creation tool.\n"
        response += "Values are provided as {id: display name}. You **always** have to use the keys (ids) as values for the quotation creation tool.\n"
        response += "Below are the products that are close matches to the product name, select the product best match with the quotationmessage.\n"
        response += f"# Products:\n{json.dumps(products)}\n"
        return response
    
    @api.model
    def _ai_partner_search(self, partner_name):
        # Search for products based on the product name to get the product ID
        partners = self.env['res.partner'].search([]).read(['name'])
        partner_list = []
        for partner in partners:
            partner_list.append(partner['name'])
        
        partners = difflib.get_close_matches(partner_name, partner_list, n=3, cutoff=0.4)
        partners = [self.env['res.partner'].search([('name', '=', partner)], limit=1)._ai_read(['name'], None) for partner in partners]
        
        response = "⚠️ Never share the info below with the user. It can only by used by you when creating a quotation with the quotation creation tool.\n"
        response += "Values are provided as {id: name}. You **always** have to use the keys (ids) as values for the quotation creation tool.\n"
        response += "Below are the partners that are close matches to the partner name, select the partner best match with the quotationmessage.\n"
        response += f"# Partners:\n{json.dumps(partners)}\n"
        return response
    
    @api.model
    def _ai_create_quotation(self, partner_id, products):
        # Create the quotation
        products = json.loads(products)
        order = self.create(self._ai_prepare_quotation_creation_values(partner_id, products))
        return f"Quotation created. Quotation ID: {order.id}"
    
    @api.model
    def _ai_prepare_quotation_creation_values(self, partner_id, products):
        # Prepare the order line values
        order_line_vals = [(0, 0, {'product_id': product['id'], 'product_uom_qty': product['quantity']}) 
                          for product in products]
        return [{
            'partner_id': partner_id,
            'user_id': self.env.ref('pshk_ai_whatsapp_quotation_b2b.user_x_whatsapp_ai_bot').id,
            'date_order': fields.Datetime.now(),
            'company_id': self.env.user.company_id.id,
            'order_line': order_line_vals
        }]
    
    @api.model
    def _ai_send_inform_message(self, order_id, message_id, success):
        # Reply to the customer's order message with the quotation number
        message = self.env['whatsapp.message'].browse(message_id)
        if message.mail_message_id.model == 'discuss.channel':
            channel = self.env['discuss.channel'].browse(message.mail_message_id.res_id)
            if success:
                order = self.browse(order_id)
                channel.message_post(body=f"🤖 Your quotation has been created. Quotation ID: {order.name}.",
                                        message_type='whatsapp_message',
                                        subtype_xmlid='mail.mt_comment',
                                        parent_id=message.mail_message_id.id)
            else:
                channel.message_post(body=f"⚠️ Your quotation has not been created. Please check the products and quantities and try again, or contact us for assistance.",
                                     message_type='whatsapp_message',
                                     subtype_xmlid='mail.mt_comment',
                                     parent_id=message.mail_message_id.id)
        return "Success"
    
    def create_quotation_from_whatsapp(self):
        # Scheduled action to create quotations from WhatsApp messages
        agent = self.env.ref('pshk_ai_whatsapp_quotation_b2b.ai_agent_x_whatsapp_quotation_b2b')
        if not agent: 
            raise UserError("WhatsApp Quotation B2B agent not found.")
        scheduled_action = self.env.ref('pshk_ai_whatsapp_quotation_b2b.ir_cron_x_whatsapp_quotation_b2b')
        if not scheduled_action:
            raise UserError("Scheduled action 'Quotation: Generate quotation from WhatsApp' not found.")
        lastcall = scheduled_action.lastcall or fields.Datetime.now()

        messages = [
            {'id': vals['id'], 'body': html2plaintext(vals['body'])}
            for vals in self.env['whatsapp.message'].search([
                ('message_type', '=', 'inbound'),
                ('create_date', '>=', lastcall),
            ]).read(['body'])
        ]
        if not messages:
            return
        
        prompt = "Below are the messages from my customers. Please identify the quotation messages and create a quotation for each message."
        prompt += f"Messages:\n{json.dumps(messages)}\n"

        # Call the AI agent to create the quotations
        response = agent._generate_response(prompt)
        return response
        