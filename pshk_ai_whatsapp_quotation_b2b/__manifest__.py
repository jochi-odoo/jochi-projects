{
    'name': 'pshk_ai_whatsapp_quotation_b2b',
    'version': '19.0.1.0.0',
    'description': 'Generate quotation from WhatsApp messages with AI for B2B clients',
    'summary': 'Generate quotation from WhatsApp messages with AI for B2B clients',
    'author': 'Odoo S.A.',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'category': 'Sales/Sales',
    'depends': [
        'ai_app',
        'sale_management',
        'whatsapp',
    ],
    'data': [
        'data/res_users.xml',
        'data/ir_actions_server_tools.xml',
        'data/ai_topics.xml',
        'data/ir_cron.xml',
        'data/ai_agent.xml'
    ],
    'auto_install': False,
    'application': False,
}
