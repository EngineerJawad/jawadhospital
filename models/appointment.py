from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointment'
    _order = "id desc"

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def get_default_note(self):
        return 1

    name = fields.Char(string='Appointment ID', required=True, copy=False,
                       readonly=True, index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True , default=get_default_note)
    notes = fields.Text(string='Registration Note')
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    appointment_date = fields.Date(string='Date', required=True)
