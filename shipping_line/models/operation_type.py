from odoo import fields, models, api


class OperationType(models.Model):
    _name = 'shipping_line.operation_type'
    _description = 'Description'
    _rec_name = 'name'
    name = fields.Char()
