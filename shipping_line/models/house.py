from odoo import fields, models, api


# from .operation import Operation


class House(models.Model):
    _name = 'shipping_line.house'
    _description = 'Description'

    name = fields.Char()
    house_bl = fields.Char(string='House B/L No.', required=True)
    operation_type = fields.Many2one(comodel_name='shipping_line.operation_type', string='Operation_type',
                                     required=False)
    port_of_discharge = fields.Many2one(comodel_name='pan_marine.port', string='Port of Discharge', required=False)
    port_terminal_of_discharge = fields.Many2one(comodel_name='shipping_line.port_terminal',
                                                 string=' Port/Terminal Discharge', required=False)
    customer = fields.Many2one(comodel_name='res.partner', string='Customer', required=False)
    rel_voyage = fields.Many2one(comodel_name='shipping_line.voyage', string='rel_voyage', required=False)
    operation_serial = fields.Char(string='Operation No.', required=False)

    # rel_agent=fields.Many2one(comodel_name='shipping_line.agent',related='rel_voyage.agent', store=True)

    @api.model
    def create(self, value_list):
        operation_obj = self.env['shipping_line.operation']
        agent = self.env['shipping_line.voyage'].search([('id', '=', value_list['rel_voyage'])]).agent
        created_obj = operation_obj.create({
            "operation_type": value_list['operation_type'],
            "voyage": value_list['rel_voyage'],
            "rel_agent": agent.id,
            "house_bl": value_list['house_bl']
        })
        value_list['operation_serial'] = created_obj.operation_seq
        obj = super(House, self).create(value_list)
        return obj

    # @api.onchange('house_bl')
    # def onchange_house_bl(self):
    #     self.operation_serial = self.env['ir.sequence'].next_by_code('code.operation.seq')
