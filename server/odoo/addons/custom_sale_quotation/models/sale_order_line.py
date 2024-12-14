# InvoiceLines/models/account_move_line.py
from odoo import models, fields, api

class SaleOrderLineCustom(models.Model):
    _inherit = 'sale.order.line'


    color = fields.Char(string="Color")
    meters = fields.Float(string="Meters")
    computed_amount = fields.Float(string="Amount", compute="_compute_amount")

    @api.depends('product_uom_qty', 'meters', 'price_unit')
    def _compute_amount(self):
        for line in self:
            line.computed_amount = line.meters * line.product_uom_qty * line.price_unit

