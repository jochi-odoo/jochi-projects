{
    'name': 'pshk_combine_lots_sn_picking_report',
    'version': '19.0.1.0.0',
    'description': 'Combine lots/serial numbers with invoice lines',
    'summary': 'Combine lots/serial numbers with invoice lines',
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'category': 'Inventory',
    'depends': [
        'stock_account',
        
    ],
    'data': [
        'models/res_company.xml',
        'models/res_config_settings.xml',
        'view/res_config_settings_views.xml',
        'view/report_invoice.xml',
    ],
    'task_id': [5979370],
}

