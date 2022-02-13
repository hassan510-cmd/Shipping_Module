from odoo import fields, models, api


class PortTerminal(models.Model):
    _name = 'shipping_line.port_terminal'
    _description = 'Description'

    name = fields.Char(required=False)
    ar_name = fields.Char(string='Arabic Name', required=False)
    rel_port = fields.Many2one(comodel_name='pan_marine.port', string='Port', required=True)
