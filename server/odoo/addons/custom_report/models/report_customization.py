from datetime import datetime
from odoo import models, fields

class CustomReportConfiguration(models.Model):
    _inherit = 'res.company'

    report_header_text = fields.Text(
        string='Report Header Text',
        help='Custom text to be displayed in document headers'
    )

    def _get_document_type_name(self, document):
        """Dynamic document type naming"""
        type_mappings = {
            'sale.order': 'Sales Quotation',
            'account.move': self._get_invoice_type_name(document)
        }
        return type_mappings.get(document._name, 'Document')

    def _get_invoice_type_name(self, invoice):
        """Determine invoice type name"""
        if invoice.move_type == 'out_invoice':
            return 'Customer Invoice'
        elif invoice.move_type == 'in_invoice':
            return 'Vendor Bill'
        elif invoice.move_type == 'out_refund':
            return 'Customer Credit Note'
        elif invoice.move_type == 'in_refund':
            return 'Vendor Credit Note'
        return 'Invoice'


    def get_formatted_date(self, date=None):
        """
        Convert date to a formatted string in the format: November 14, 2024.
        If no date is provided, use the current date.
        :param date: Date to be formatted
        :return: Formatted date string
        """
        if date is None:
            date = datetime.today()  # Use the current date if none is provided
        return date.strftime('%B %d, %Y')

    

    def get_award_image_path(self):
        """
        Returns the path to the award image if it exists
        :return: Image path or False
        """
        import os
        award_image_path = '/custom_report/static/src/img/company_award.png'
        full_path = os.path.join(
            os.path.dirname(__file__), 
            '../static/src/img/company_award.png'
        )
        return award_image_path if os.path.exists(full_path) else False


    def get_document(self, o=None, doc=None):
        """
        Retrieve document from either o or doc
        """
        # Check account move (invoice)
        if o and o._name == 'account.move':
            return o
        
        # Check sale order (quotation)
        if doc and doc._name == 'sale.order':
            return doc
        
        return False
    
    def get_document_type_name(self, document):
        """
        Dynamic document type naming
        """
        if not document:
            return 'Unknown Document'
        
        # Detailed type mappings
        type_mappings = {
            # Invoice types
            ('account.move', 'out_invoice'): 'Customer Invoice',
            ('account.move', 'in_invoice'): 'Vendor Bill',
            ('account.move', 'out_refund'): 'Customer Credit Note',
            ('account.move', 'in_refund'): 'Vendor Credit Note',
            
            # Quotation types
            ('sale.order', None): 'Sales Quotation',
            ('purchase.order', None): 'Purchase Quotation'
        }
        
        # Get the key for lookup
        key = (
            document._name, 
            document.move_type if document._name == 'account.move' else None
        )
        
        # Return mapped name or fallback
        return type_mappings.get(key, f"{document._name} Document")