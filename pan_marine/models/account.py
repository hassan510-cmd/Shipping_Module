from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    account_custom_field = fields.Char()
    rel_inquiry = fields.Many2one(comodel_name='pan_marine.inquiry')
    product_price = fields.Float(string='Product Price', related='product_id.lst_price', required=False)
