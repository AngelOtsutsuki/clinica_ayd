from odoo import models, fields, api # type: ignore

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_patient = fields.Boolean(string="¿Es paciente?", default=False)
    numero_cuenta = fields.Char(string='Número de Cuenta', unique=True)
    edad = fields.Integer(string='Edad')
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    ], string='Género')
    historial_medico = fields.Text(string='Historial Médico')
