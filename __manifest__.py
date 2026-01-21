# -*- coding: utf-8 -*-
{
    'name': "hr_employee_es_id",

    'summary': "Extensión de hr.employee para identificación española (NSS y DNI)",

    'description': """
Extensión del módulo hr.employee para incluir:
- Número de Seguridad Social (NSS)
- DNI con validación de letra de control
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

