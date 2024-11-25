from odoo import models, fields, api # type: ignore

class InicioMedico(models.TransientModel):
    _name = 'inicio.medico'
    _description = 'Ventana de Inicio para Expedientes Médicos'

    numero_cuenta = fields.Char(string='Número de Cuenta')

    def action_buscar_paciente(self):
        if not self.numero_cuenta:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Error',
                    'message': 'Por favor, ingresa un número de cuenta para buscar.',
                    'type': 'danger',
                    'sticky': False,
                },
            }

        paciente = self.env['expediente.paciente'].search([('numero_cuenta', '=', self.numero_cuenta)], limit=1)
        if paciente:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Paciente',
                'res_model': 'expediente.paciente',
                'view_mode': 'form',
                'res_id': paciente.id,
                'target': 'current',
            }
        else:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'No encontrado',
                    'message': f'No se encontró un paciente con el número de cuenta {self.numero_cuenta}.',
                    'type': 'warning',
                    'sticky': False,
                },
            }

    def action_agregar_paciente(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Agregar Paciente',
            'res_model': 'expediente.paciente',
            'view_mode': 'form',
            'context': {'default_is_patient': True},
            'target': 'current',
        }

    def action_salir(self):
        return {'type': 'ir.actions.client', 'tag': 'home'}
