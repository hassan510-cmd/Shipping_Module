from odoo import fields, models, api


class ServiceProduct(models.Model):
    _name = 'pan_marine.services_products'
    _description = 'Description'
    _inherits = {'account.move.line': "invoice_line_ids"}
    # _inherit = ['account.move']
    rel_inquiry = fields.Many2one(comodel_name="pan_marine.inquiry", string='inquiry')
    quantity = fields.Float(
        string='Quantity',
        default='1.00',
        required=False)
    transaction_ids = fields.Char(string='transaction_ids ')
    # name = fields.Char(
    #     string='Name',
    #     required=False)
    # product_id = fields.Many2one(
    #     'product.product', 'Product Variant',
    #     check_company=True, index=True)
#     _description = 'Description'
#     # _inherits = {'product.product': "name"}
#     _inherits = {'product.product': "product_tmpl_id"}

# class ProductProduct(models.Model):
#     _name = "product.product"
#     _description = "Product"
#     _inherits = {'product.template': 'product_tmpl_id'}
# _inherit = ['account.move']
