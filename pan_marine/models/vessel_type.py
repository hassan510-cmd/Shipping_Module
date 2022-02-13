from odoo import fields, models, api


class VesselType(models.Model):
    _name = 'pan_marine.vessel_type'
    _description = 'pan marine vessels type '
    _rec_name = 'type'
    type = fields.Char(required=True)
