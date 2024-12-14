{
    'name': 'Custom Report Layouts',
    'version': '1.0',
    'summary': 'Custom Layout for Invoices and Sales Quotations',
    'description': """
        This module provides a custom report layout for invoices and sales quotations, 
        featuring a centered image, company details, and styled headers.
    """,
    'category': 'Generic Modules',
    'author': 'Idah Guantai',
    'website': 'https://github.com/idah-github',
  'depends': ['base', 'web', 'sale', 'account'],
    'data': [
        'views/custom_report_template.xml',
        'views/custom_report_inherantance.xml',
    ],
 
    'assets': {
        'web.report_assets_common': [
            '/doc_layout/static/src/img/your_image.png',  # Include the image in assets if needed
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

