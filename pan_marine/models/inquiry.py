# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Inquiry(models.Model):
    _name = "pan_marine.inquiry"
    _description = "inquiry and canceled jobs"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _rec_name = 'inquiry_number'
    inquiry_number = fields.Char(string='Inquiry Number', required=False, copy=False,
                                 readonly=True,
                                 tracking=True,
                                 default='new')
    customer = fields.Many2one(string="Customer", required=False, comodel_name='res.partner',
                               tracking=True)
    agent_Role = fields.Selection([
        ('empty', ' '),
        ('full_agent', 'Full Agent'),
        ('protecting_agent', "Protecting Agent"),
        ('husbandry_agent', "Husbandry Agent"),
        ('oil_gas_services', 'Oil & Gas Services')
    ], string="Agent Role", required=True)
    attention = fields.Char(string="Requested By/Attention", required=True)
    address = fields.Char(string="Requested By/Address", required=False)
    bank = fields.Many2one('res.bank', string="Requested By/Bank")
    voyage_number = fields.Char(string="Voyage No", required=True)
    vessel_name = fields.Many2one(string="Vessel Name", required=True, comodel_name='pan_marine.vessel')
    imo = fields.Char(string="IMO", required=False, readonly=True, default=0, related='vessel_name.IMO')
    requested_date = fields.Datetime(string='Requested Date', required=True)
    port = fields.Many2one(comodel_name='pan_marine.port', string='Port', required=True)
    berth = fields.Char(string="Berth", required=False)
    ETA = fields.Datetime(string='ETA', required=True)
    ETD = fields.Datetime(string='EDA', required=False)
    call_type = fields.Many2one(string="Call Type", required=False, comodel_name='pan_marine.call')
    currency = fields.Many2one('res.currency', string='Currency', required=True)
    notes = fields.Text(string='Notes', required=False)
    created_by = fields.Char(
        string='User',
        compute='_compute_get_creator_name',
    )
    follow = fields.One2many(
        comodel_name='pan_marine.follow_up',
        inverse_name='rel_inquiry',
        string='Follow',
        required=False)
    state = fields.Selection(
        [
            ('draft', 'Draft Inquiry'),
            ('sent', 'Inquiry Sent'),
            ('appointment', ' Appointment '),
            ('OC', ' Operationally Closed '),
            ('FC', ' Financially Closed '),
        ], string='Status', required=False, readonly=True
    )
    # invoice_lines = fields.One2many(
    #     comodel_name='pan_marine.services_products',
    #     inverse_name='id',
    #     string='Invoice_lines',
    #     required=False)
    # invoice_lines = fields.One2many(
    #     comodel_name='pan_marine.services_products',
    #     inverse_name='product_id',
    #     string='Invoice_lines',
    #     required=False)
    # product_id = fields.Many2one(
    #     'product.product', 'Product Variant',
    #     check_company=True, index=True)
    product_id = fields.One2many(
        inverse_name='rel_inquiry',
        comodel_name='account.move.line',
        string='Invoice_lines',
        required=False)

    @api.model
    def create(self, value_list):
        value_list[
            'inquiry_number'] = f"{self.env['ir.sequence'].next_by_code('code.inquiry.seq')}/{datetime.now().year}"
        obj = super(Inquiry, self).create(value_list)
        return obj

    def _compute_get_creator_name(self):
        print(self.env.user.name)
        for rec in self:
            username = rec.env['res.users'].search([("id", '=', rec.create_uid.id)]).login
            rec.created_by = f"{username}".title()
