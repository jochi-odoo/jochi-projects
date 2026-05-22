from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_company_ids = fields.Many2many('res.company', string='Companies Visibility')

    def _get_redirect_suggested_company(self):
        # 1. First, try the standard logic
        suggested = super()._get_redirect_suggested_company()
        if suggested:
            return suggested
        # 2. If standard logic fails, look at your custom field
        if 'x_company_ids' in self and self.x_company_ids:
            # Return the first company in your custom list that the user is allowed to see
            return (self.x_company_ids & self.env.user.company_ids)[:1]
            
        return False
