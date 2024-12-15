{
    'name': 'Customizing Document Reports',
    'version': '1.0',
    'summary': 'Customized Quotation and Invoice Reports',
    'description': 'Enhanced reporting layout for: Sales Quotations, Customer Invoices and Vendor Bills',
    'author': 'Idah Guantai',
    'website': 'https://github.com/idah-github',
    'depends': ['base', 'web', 'sale', 'account'],
    'data': [
        'views/report_external_layout.xml',
        'views/report.xml',
        'views/sale_order_report_templates.xml',
        'views/account_move_report_templates.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            '/custom_report/static/src/css/custom_report.css',
        ],
    },
    'installable': True,
    'application': False, 
    'auto_install': False,
}
