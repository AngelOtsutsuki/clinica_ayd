
from odoo import models, fields, api # type: ignore

class Medicamento(models.Model):
    _name = 'cl_stock.medicamento'
    _description = 'Medicamento'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    cantidad = fields.Integer(string="Cantidad en inventario", default=0)
    precio_unitario = fields.Float(string="Precio Unitario", required=True)
    fecha_caducidad = fields.Date(string="Fecha de Caducidad")

    @api.model
    def actualizar_cantidad(self, cantidad, tipo):
         """
         Actualiza la cantidad del medicamento.
         :param cantidad: Cantidad a sumar o restar.
         :param tipo: 'agregar' o 'restar'.
         """
         if tipo == 'agregar':
             self.cantidad += cantidad
         elif tipo == 'restar' and self.cantidad >= cantidad:
             self.cantidad -= cantidad
         else:
             raise ValueError("Cantidad insuficiente en el inventario.")