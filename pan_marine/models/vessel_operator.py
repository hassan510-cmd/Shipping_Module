from odoo import fields, models, api


class VesselOperator(models.Model):
    _name = 'pan_marine.vessel_operator'
    _description = 'pan marine vessel operator'
    _rec_name='name'
    name = fields.Char(string='Operator Name')
    country = fields.Many2one(
        comodel_name='res.country',
        string='Operator Country',
        required=False)
