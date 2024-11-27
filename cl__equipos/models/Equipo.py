from odoo import models, fields, api # type: ignore

class Equipo(models.Model): 
    _name = 'cl_equipos.equipo'
    _description = 'Equipo'

    name = fields.Char(string="Nombre", required=True)
    estado = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')], string="Estado", required=True)
    cantidad = fields.Integer(string="Cantidad en inventario", default=0)
    ubicacion = fields.Char(string="Ubicación")
    fecha_ultimo_mantenimiento = fields.Date(string="Fecha de Último Mantenimiento")

    @api.model
    def actualizar_cantidad(self, cantidad, tipo):
         """
         Actualiza la cantidad del equipo.
         :param cantidad: Cantidad a sumar o restar.
         :param tipo: 'agregar' o 'restar'.
         """
         if tipo == 'agregar':
             self.cantidad += cantidad
         elif tipo == 'restar' and self.cantidad >= cantidad:
             self.cantidad -= cantidad
         else:
             raise ValueError("Cantidad insuficiente en el inventario.")
