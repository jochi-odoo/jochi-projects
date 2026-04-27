{
    'name': 'pshk_crm_lead_line',
    'version': '19.0.1.0.0',
    'description': 'Track products in CRM opportunities and transfer directly to sales order',
    'summary': 'Track products in CRM opportunities and transfer directly to sales order',
    'author': 'Odoo S.A.',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'category': 'CRM/CRM',
    'depends': [
        'sale_crm'
    ],
    'data': [
        'models/res_company.xml',
        'models/res_config_settings.xml',
        'models/x_crm_lead_line.xml',
        'models/crm_lead.xml',
        'security/ir.model.access.csv',
        'data/server_action.xml',
        'view/res_config_settings_views.xml',
        'view/crm_lead_views.xml',
        'view/crm_opportunity_to_quotation_views.xml',
    ],
    'auto_install': False,
    'application': False,
    'task_id': [6021762],
}
