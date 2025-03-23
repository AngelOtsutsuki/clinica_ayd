from odoo import models, fields

class CitaMedica(models.Model):
    _name = 'expediente.citamedica'
    _description = 'Citas Médicas'

    paciente_id = fields.Many2one('res.partner', string='Paciente', required=True, ondelete='cascade', domain=[('is_patient', '=', True)])
    fecha_cita = fields.Datetime(string='Fecha y Hora', required=True)
    motivo = fields.Char(string='Motivo de la Cita', required=True)
    doctor = fields.Char(string='Doctor')
    diagnostico = fields.Text(string='Diagnóstico')
    tratamiento = fields.Text(string='Tratamiento')
