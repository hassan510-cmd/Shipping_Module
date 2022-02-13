from odoo import fields, models, api


class CargoRate(models.Model):
    _name = 'pan_marine.cargo_rate'
    _description = 'Description'

    name = fields.Many2one(
        comodel_name='pan_marine.cargo',
        string='Cargo Name',
        required=False)
    
    port = fields.Many2one(
        comodel_name='pan_marine.port',
        string='Port',
        required=False)
    
    rate = fields.Char(
        string='Rate', 
        required=False)
