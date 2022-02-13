from odoo import models, fields, api


class Ports(models.Model):
    _name = "pan_marine.port"
    _description = "pan marine ports"
    _rec_name = "name"
    name = fields.Char(
        string='Port Name',
        required=True)

    code = fields.Char(
        string='Port Code',
        required=True)

    country = fields.Many2one(
        comodel_name='res.country',
        string='Country',
        required=True)

    country_code = fields.Char(
        string='Country Code',
        related='country.code',
        required=False,
        readonly=True)
