from odoo import fields, models, api


class Call(models.Model):
    _name = 'pan_marine.call'
    _description = 'Description'

    name = fields.Char()
