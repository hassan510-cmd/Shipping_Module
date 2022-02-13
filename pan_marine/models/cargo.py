from odoo import fields, models, api


class Cargo(models.Model):
    _name = 'pan_marine.cargo'
    _description = 'Description'
    _rec_name = 'name'
    name = fields.Char()
