# -*- coding: utf-8 -*-
{
    'name': "Shipping",
    'application': True,
    'sequence': 1,
    'summary': """
        pan marine module """,

    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/pan_marine.xml',
        'views/inquiry.xml',
        'views/templates.xml',
        'data/pan_marine_sequence.xml',
        'views/port.xml',
        'views/vessel_type.xml',
        'views/vessel_operator.xml',
        'views/canal_vessel_type.xml',
        'views/vessel.xml',
        'views/cargo.xml',
        'views/cargo_rate.xml',
        'views/berth_cargo.xml',
        'views/berth.xml',
        'views/call.xml',
        'views/follow_up_type.xml',
        'views/follow_up.xml',
        'views/services_products.xml',
        'views/account.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
