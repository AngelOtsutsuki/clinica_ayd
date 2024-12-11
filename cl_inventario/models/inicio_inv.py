from odoo import models, fields, api # type: ignore

class Inicio_Inv(models.Model):
    _name = 'cl_inventario.inicio_inv'
    _description = 'Pantalla de Inicio de Inventario'

    name = fields.Char(string="Nombre", default="Inventario", readonly=True)

    def inventario_equipos(self):
    # Método temporal para el botón de Inventario
        return {
        'type': 'ir.actions.act_window',
        'name': 'Equipos',
        'res_model': 'cl_equipos.equipo',
        'view_mode': 'list,form',
        'target': 'current',
        }

    def inventario_medicamentos(self):
    # Método temporal para el botón de Inventario
        return {
        'type': 'ir.actions.act_window',
        'name': 'Medicamentos',
        'res_model': 'cl_stock.medicamento',
        'view_mode': 'list,form',
        'target': 'current',
        }