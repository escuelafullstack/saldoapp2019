# -*- coding: utf-8 -*-
{
    'name': "Saldo APP",

    'summary': """
        Módulo para gestionar los ingresos y egresos de los usuarios""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Escuela FULLSTACK",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/sa_categoria.xml',
        'security/group_administrador.xml',
        'security/group_usuario.xml',
        'security/group_usuario_premium.xml',

        'views/views.xml',
        'views/templates.xml',
        'views/view_diario.xml',
        'views/view_categoria.xml',
        'views/view_movimientos.xml',
        'views/res_partner.xml',
        'views/menu.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}