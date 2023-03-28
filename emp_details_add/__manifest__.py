# -*- coding: utf-8 -*-
{
    'name': "emp_details_add",

    'summary': """
        Adds new fields to the Employee model""",

    'description': """
    This module adds new fields to the Employee model, including:
        - Skills/Area
        - Project Name
        - Project Start Date
        - Project End Date
        - HR POC
        - PM
        - PPM
        - Experience    """,

    'author': "Leuwint Technology",
    'website': "https://www.leuwint.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/work_location_views.xml',
        
    ],
    'installable': True,
    'auto_install'  : False,
   # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml', 
    # ],
    
}
