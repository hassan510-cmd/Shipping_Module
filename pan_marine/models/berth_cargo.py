from odoo import fields, models, api


class BerthCargo(models.Model):
    _name = 'pan_marine.berth_cargo'
    _description = 'Description'
    _inherit = 'pan_marine.cargo'

