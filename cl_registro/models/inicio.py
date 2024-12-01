from odoo import models, fields, api

class Inicio(models.Model):
    _name = 'cl_registro.inicio'
    _description = 'Pantalla de Inicio'

    name = fields.Char(string="Nombre", default="Inicio", readonly=True)

    def dummy_inventario(self):
        # Método temporal para el botón de Inventario
        pass

    def abrir_expediente(self):
        # Método para redirigir al módulo expediente
        return {
            'type': 'ir.actions.act_window',
            'name': 'Pacientes',
            'res_model': 'expediente.paciente',  # El modelo de pacientes en expediente
            'view_mode': 'list,form',  # Tipo de vistas que quieres mostrar
            'target': 'current',  # Muestra en la misma ventana
        }
