# InvoiceLines/__manifest__.py
{
    'name': 'Sale Order Line Custom Fields',
    'version': '1.0',
    'summary': 'Adds custom fields and structure to quotation lines.',
    'description': 'This module customizes sales order lines by adding fields such as color, meters, VAT, and computes custom amounts.',
    'author': 'Idah Guantai',
    'category': 'Sales',
    'depends': ['sale',
                'account',
                'web',
                ],
    'data': [
        'views/sale_order_views.xml',
        'views/report_sales_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

