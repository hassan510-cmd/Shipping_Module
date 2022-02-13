from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    hassan_name = fields.Char()
    rel_inquiry = fields.Many2one(comodel_name='pan_marine.inquiry')
