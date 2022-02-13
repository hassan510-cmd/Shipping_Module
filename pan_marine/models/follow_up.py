from odoo import fields, models, api


class FollowUp(models.Model):
    _name = 'pan_marine.follow_up'
    _description = 'Description'

    created_by = fields.Many2one(comodel_name='res.users', string='Created By', required=False)
    follow_type = fields.Many2one(comodel_name='pan_marine.follow_up_type', string='Type', required=False)
    start_date = fields.Datetime(string='Start Date', required=False)
    remarks = fields.Text(string="Remarks", required=False)
    rel_inquiry = fields.Many2one(comodel_name="pan_marine.inquiry", string='inquiry')
