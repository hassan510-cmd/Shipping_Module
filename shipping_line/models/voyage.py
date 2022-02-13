from odoo import fields, models, api
from datetime import datetime


class Voyage(models.Model):
    _name = 'shipping_line.voyage'
    _description = 'Description'
    _rec_name = 'voyage_seq'

    voyage_seq = fields.Char(string='Voyage Seq', required=False, copy=False,
                             readonly=True, tracking=True, default='new')
    number = fields.Char(string='Voyage Number', required=True)
    discharge_port = fields.Many2one(comodel_name='pan_marine.port', string='Discharge Port', required=False)
    terminal_port = fields.Many2one(comodel_name='shipping_line.port_terminal', string='Terminal Port', required=False)
    port_of_loading = fields.Many2one(comodel_name='pan_marine.port', string='Port of Loading', required=False)
    port_terminal_of_loading = fields.Many2one(comodel_name='shipping_line.port_terminal',
                                               string=' Port/Terminal Loading', required=False)
    rel_vessel = fields.Many2one(comodel_name='pan_marine.vessel', string='Vessel', required=True)
    shipping_line = fields.Char(string='Shipping_line', required=False)
    agent = fields.Many2one(comodel_name='shipping_line.agent', string='Agent', required=False)
    arrival_date = fields.Datetime(string='Arrival Date', required=True)
    discharge_date = fields.Datetime(string='Discharge Date', required=True)
    storage_free_days = fields.Integer(string='Storage Free Days', required=False)
    demurrage_free_days = fields.Integer(string='Demurrage Free Days', required=False)
    total_gross_weight = fields.Float(string='Total Gross Weight(KGS)', readonly=True, required=False)
    total_no_of_containers = fields.Float(string='Total No. of Containers', readonly=True, required=False)
    rel_operation = fields.One2many(comodel_name='shipping_line.operation', inverse_name='voyage',
                                    string='Rel_operation', required=False)
    rel_house = fields.One2many(comodel_name='shipping_line.house', inverse_name='rel_voyage',
                                string='House info', required=False)

    @api.model
    def create(self, value_list):
        value_list[
            'voyage_seq'] = f"{self.env['ir.sequence'].next_by_code('code.voyage.seq')}/{datetime.now().year}"
        obj = super(Voyage, self).create(value_list)

        return obj