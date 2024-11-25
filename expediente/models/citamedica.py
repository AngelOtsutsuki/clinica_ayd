from odoo import models, fields, api # type: ignore

class CitaMedica(models.Model):
    _name = 'expediente.citamedica'
    _description = 'Citas Médicas'
    #_inherit = 'expediente.paciente'

    paciente_id = fields.Many2one('expediente.paciente', string='Paciente', required=True, ondelete='cascade')
    fecha_cita = fields.Datetime(string='Fecha y Hora', required=True)
    motivo = fields.Text(string='Motivo de la Cita', required=True)
    doctor = fields.Char(string='Doctor')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='pendiente', required=True)