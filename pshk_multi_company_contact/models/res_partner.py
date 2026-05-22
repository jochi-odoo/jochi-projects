from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_company_ids = fields.Many2many('res.company', string='Companies Visibility')

    def _get_redirect_suggested_company(self):
        self.ensure_one()

        if 'x_company_ids' in self and self.x_company_ids:
            return (self.x_company_ids & self.env.user.company_ids)[:1]
            
        return super()._get_redirect_suggested_company()
