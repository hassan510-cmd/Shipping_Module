import datetime

from odoo import fields, models, api
from datetime import datetime


class Operation(models.Model):
    _name = 'shipping_line.operation'
    _description = 'Description'
    _rec_name = 'operation_seq'

    operation_seq = fields.Char(string='Operation Seq', required=False, copy=False,
                                readonly=True, tracking=True, default='new')
    customer = fields.Many2one(comodel_name='res.partner', string='Customer', required=False)
    voyage = fields.Many2one(comodel_name='shipping_line.voyage', required=False)
    house_bl = fields.Char(string='House B/L No.', required=True)
    port_of_loading = fields.Many2one(comodel_name='pan_marine.port', string='Port of Loading', required=False)
    port_of_discharge = fields.Many2one(comodel_name='pan_marine.port', string='Port of Discharge', required=False)
    port_terminal_of_discharge = fields.Many2one(comodel_name='shipping_line.port_terminal',
                                                 string=' Port/Terminal Discharge', required=False)
    port_terminal_of_loading = fields.Many2one(comodel_name='shipping_line.port_terminal',
                                                         string=' Port/Terminal Loading', required=False)
    deliver_data = fields.Datetime(string='Deliver Data', required=False)
    empty_return_date = fields.Datetime(string='Empty Return Date', required=False)
    discharge_type = fields.Char(string='Discharge_type', required=False)
    rel_agent = fields.Many2one(comodel_name='shipping_line.agent', string='Agent', required=False)
    freight = fields.Many2one(comodel_name='shipping_line.freight')
    actual_delivery_date = fields.Datetime(string='Actual Delivery Date', required=False)
    requested_date = fields.Datetime(string='Requested Date', required=False)
    storage_free_days = fields.Integer(string='Storage Free Days', related='voyage.storage_free_days', required=False)
    demurrage_free_days = fields.Integer(string='Demurrage Free Days', related='voyage.demurrage_free_days',
                                         required=False)
    general_description = fields.Text(string="General Description", required=False)
    total_no_of_containers = fields.Float(string='Total No. of Containers', related='voyage.total_no_of_containers',
                                          readonly=True, required=False)
    total_gross_weight = fields.Float(string='Total Gross Weight(KGS)', related='voyage.total_gross_weight',
                                      readonly=True, required=False)
    TUE = fields.Integer(readonly=True, string='TUE', required=False)
    total_no_of_packages = fields.Float(string='Total No of Packages', readonly=True, required=False)
    type_of_packages = fields.Char(readonly=True, string='Type of Packages', required=False)
    total_chargeable_weight = fields.Float(string='Total Chargeable Weight(KGS)', readonly=True, required=False)
    total_volume = fields.Float(readonly=True, string='Total Volume(CBM)', required=False)
    total_freight_ton = fields.Float(readonly=True, string='Total Freight Ton', required=False)
    # rel_voyage = fields.Many2one(comodel_name='shipping_line.voyage', string=' rel_voyage', required=False)
    # rel_voyage_op=fields.Many2one(comodel_name="shipping_line.voyage")
    operation_type = fields.Many2one(comodel_name='shipping_line.operation_type', string='operation type')
    state = fields.Selection(
        [
            ('draft', 'Draft Offer'),
            ('sent', 'Offer Sent'),
            ('operation', ' Operation '),
            ('OC', ' Operationally Closed '),
            ('FC', ' Financially Closed '),
        ], string='Status', required=False, readonly=True
    )

    @api.model
    def create(self, value_list):
        value_list[
            'operation_seq'] = f"{self.env['ir.sequence'].next_by_code('code.operation.seq')}/{datetime.now().year}"
        obj = super(Operation, self).create(value_list)
        return obj
