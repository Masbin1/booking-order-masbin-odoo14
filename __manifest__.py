# -*- coding: utf-8 -*-
{
    'name': "booking_order_bintang_odoo14",

    'summary': """
        Booking Order Bintang""",

    'description': """
        Booking Order Bintang 14
    """,

    'author': "Mas Bintang",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/wo_sequence.xml',
        'views/menu_item.xml',
        'views/sale_order.xml',
        'views/service_team.xml',
        'views/work_order.xml',
        'wizard/cancel_state.xml',
        'report/work_order_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
