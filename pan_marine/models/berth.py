from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'pan_marine.berth'
    _description = 'Description'

    port = fields.Many2one(comodel_name='pan_marine.port', string='Port', required=True)
    name = fields.Char(string='Berth Name', required=True)
    draft = fields.Float(string='Draft', required=False)
    draft_unit = fields.Many2one(comodel_name='uom.uom', string='Draft Unit', required=False)
    LOA = fields.Float(string='LOA', required=False)
    length_unit = fields.Many2one(comodel_name='uom.uom', string='Length Unit', required=False)
    cargo = fields.Many2one(comodel_name='pan_marine.cargo', string='Cargo', required=False)
