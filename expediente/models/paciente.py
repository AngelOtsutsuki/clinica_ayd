# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore

class Paciente(models.Model):
    _name = 'expediente.paciente'
    # _inherit = 'res.partner'
    _description = 'Pacientes del sistema médico'
    
    tipo_pac = fields.Selection([
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
        ('visitante', 'Visitante'),
    ], string='Tipo de Paciente')
    nombres = fields.Char(string='Nombres')
    apellidos = fields.Char(string='Apellidos')
    numero_cuenta = fields.Char(string='Número de Cuenta', required=True, unique=True)
    identidad = fields.Char(string='Número de Identidad')
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    ], string='Género')
    fecha_nac = fields.Date(string='Fecha de Nacimiento', required=True, unique=True)
    edad = fields.Integer(string='Edad')
    correo_inst = fields.Char(string='Correo Institucional')
    telefono = fields.Char(string='Teléfono')
    alergias = fields.Text(string='Alergias')
    med_act = fields.Text(string='Medicamenos Actuales')
    enf_pre = fields.Text(string='Enfermedades Preexistentes')
    nombre_cont = fields.Char(string='Nombre del Contacto')
    relacion = fields.Char(string='Relación')
    telefono_cont = fields.Char(string='Número de Teléfono')
    telefono_cont2 = fields.Char(string='Otro Teléfono')
    citas_ids = fields.One2many('expediente.citamedica', 'paciente_id', string='Cita Médica')
    #historial_medico = fields.Text(string='Historial Médico')

    #  @api.model
    #  def create(self, vals):
    #      # Agregar lógica personalizada, por ejemplo, para validar el número de cuenta
    #      if 'numero_cuenta' in vals:
    #          if self.search([('numero_cuenta', '=', vals['numero_cuenta'])]):
    #              raise ValueError('El número de cuenta ya está en uso.')
    #      return super(Paciente, self).create(vals)
    
    #  def action_guardar_cambios(self):
        
    #      # Método para guardar los cambios en el registro actual.
        
    #      self.ensure_one()  # Garantiza que se esté trabajando con un único registro.
    #      self.write({
    #          'name': self.name,
    #          'numero_cuenta': self.numero_cuenta,
    #          'edad': self.edad,
    #          'genero': self.genero,
    #          'historial_medico': self.historial_medico,
    #          })
    #      return {
    #          'type': 'ir.actions.client',
    #          'tag': 'reload',
    #      }



