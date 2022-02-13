from odoo import fields, models, api


class Freight(models.Model):
    _name = 'shipping_line.freight'
    _description = 'Description'

    name = fields.Char()
