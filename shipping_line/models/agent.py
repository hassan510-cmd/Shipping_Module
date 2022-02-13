from odoo import fields, models, api


class Agent(models.Model):
    _name = 'shipping_line.agent'
    _description = 'Description'

    name = fields.Char()
    ar_name = fields.Char(
        string='Arabic Name',
        required=False)

    header_image = fields.Binary(string="Header Image")
    footer_image = fields.Binary(string="Footer Image")
