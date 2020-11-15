# -*- coding: utf-8 -*-
{
    'name': "HoGy",

    'summary': """todo""",

    'description': """
        todo
    """,

    'author': "Olti Dajce",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/person/coach.xml',
        'views/person/disciple.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}