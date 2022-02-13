from odoo import fields, models, api


class CanalVesselType(models.Model):
    _name = 'pan_marine.canal_vessel_type'
    _description = 'pan marine Canal vessels type '
    _inherit = 'pan_marine.vessel_type'
