from odoo import models, api, fields
from datetime import date

class CustomReportSaleOrder(models.AbstractModel):
    _name = 'report.custom.sale.order'
    _description = 'Custom Sale Order Report'
    
    current_date = fields.Date(string='Current Date', compute='_compute_current_date')

    @api.depends()
    def _compute_current_date(self):
        for record in self:
            record.current_date = fields.Date.today()

    @api.model
    def _get_report_values(self, docids, data=None):
        # Fetch sale orders
        sale_orders = self.env['sale.order'].browse(docids)
        
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': sale_orders,
            'company': self.env.company,
            'current_date': self.current_date,
            'custom_data': self._prepare_report_data(sale_orders)
        }


    def _prepare_report_data(self, sale_orders):
        """
        Prepare custom report data
        """
        custom_data = {}
        for order in sale_orders:
            custom_data[order.id] = {
                'formatted_date': order.date_order.strftime('%Y-%m-%d'),
                'total_weight': sum(line.product_id.weight * line.product_uom_qty for line in order.order_line),
                'special_instructions': order.note or ''
            }
        return custom_data

