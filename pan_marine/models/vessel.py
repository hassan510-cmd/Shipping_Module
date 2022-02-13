from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'pan_marine.vessel'
    _description = 'Description'
    _rec_name = 'name'

    IMO = fields.Char(string='IMO', required=False)
    name = fields.Char(string='Vessel Name', required=False)
    flag = fields.Many2one(comodel_name='res.country', string='Flag', required=False)
    dead_weight = fields.Integer(string='Dead Weight', required=False)
    gross_weight = fields.Integer(string='Gross Weight', required=False)
    operator_name = fields.Many2one(comodel_name='pan_marine.vessel_operator', string='Operator Name', required=False)
    operator_country = fields.Char(string='Operator Country', required=False, readonly=True,
                                   related='operator_name.country.name')
    year_built = fields.Date(string='Year Built', required=False)
    vessel_type = fields.Many2one(comodel_name='pan_marine.vessel_type', string='Vessel Type',
                                  required=False)
