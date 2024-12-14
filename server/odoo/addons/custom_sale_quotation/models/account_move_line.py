# InvoiceLines/models/account_move_line.py
from odoo import models, fields, api

class AccountMoveLineCustom(models.Model):
    _inherit = 'account.move.line'
    
    color = fields.Char(string="Colour")
    meters = fields.Float(string="Meters")
    # vat = fields.Float(string="VAT (%)")
    #discount = fields.Float(string="Discount (%)")
    computed_amount = fields.Float(string="Amount", compute="_compute_amount")

    # @api.depends('meters', 'product_uom_qty', 'price_unit')
    # def _compute_amount(self):
    #     for line in self:
    #         line.computed_amount = line.meters * line.product_uom_qty * line.price_unit
            # discount_amount = base_amount * (line.discount / 100)
            # line.computed_amount = base_amount - discount_amount
