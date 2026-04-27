{
    'name': 'pshk_prevent_negative_selling',
    'version': '19.0.1.0.0',
    'description': 'Block transfers with negative on-hand quantity',
    'summary': 'Block transfers with negative on-hand quantity',
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'category': 'Inventory',
    'depends': [
        'stock'
    ],
    'data': [
        'models/stock_picking_type.xml',
        'data/server_action.xml',
        'view/stock_picking_type_views.xml',
        'view/stock_picking_views.xml',
    ],
    'task_id': [4383541],
}
