# InvoiceLines/models/account_move_line.py
from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    color = fields.Char(string="Colour")
    meters = fields.Float(string="Meters")
    # vat = fields.Float(string="VAT (%)")
    # discount = fields.Float(string="Discount (%)")
    computed_amount = fields.Float(string="Amount", compute="_compute_amount")

    @api.depends('meters', 'quantity', 'price_unit')
    def _compute_amount(self):
        for line in self:
            line.computed_amount = line.meters * line.quantity * line.price_unit
            
    def _get_formatted_date(self, date):
        """
        Convert date to a formatted string in the format: November 14, 2024
        :param date: Date to be formatted
        :return: Formatted date string
        """
        if not date:
            return ''
        return date.strftime('%B %d, %Y')

