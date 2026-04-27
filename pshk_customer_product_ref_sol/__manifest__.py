{
    'name': 'pshk_customer_product_ref_sol',
    'version': '19.0.1.0.0',
    'description': 'Enable customer product reference information on sales order lines',
    'summary': 'Enable customer product reference information on sales order lines',
    'author': 'Odoo S.A.',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'category': 'Sales/Sales',
    'depends': [
        'sale'
    ],
    'data': [
        'models/x_external_reference.xml',
        'models/sale_order_line.xml',
        'view/x_external_reference_views.xml',
        'view/sale_order_views.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': False,
    'application': False,
    'task_id': [6012292],
}
