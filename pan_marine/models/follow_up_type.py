from odoo import fields, models, api


class FollowUpType(models.Model):
    _name = 'pan_marine.follow_up_type'
    _description = 'Description'
    _rec_name = 'type'
    type = fields.Char(string='Follow Up Name', required=True)

