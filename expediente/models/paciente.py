# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions # type: ignore

class Paciente(models.Model):
    _name = 'expediente.paciente'
    # _inherit = 'res.partner'
    _description = 'Pacientes del sistema médico'
    
    tipo_pac = fields.Selection([
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
        ('visitante', 'Visitante'),
        ('personal administrativo', 'Personal Administrativo'),
        ('personal de servicio', 'Personal de Servicio'),
    ], string='Tipo de Paciente')
    numero_empleado = fields.Char(string='Número de Empleado', help="Requerido si el paciente es docente o personal administrativo/servicio.")
    nombres = fields.Char(string='Nombres')
    apellidos = fields.Char(string='Apellidos')
    numero_cuenta = fields.Char(string='Número de Cuenta', unique=True)
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    ], string='Género')
    fecha_nac = fields.Date(string='Fecha de Nacimiento', required=True, unique=True)
    edad = fields.Integer(string='Edad', compute="_compute_edad", store=True)
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

    @api.depends('fecha_nac')
    def _compute_edad(self):
        """Calcula la edad del paciente en base a su fecha de nacimiento."""
        from datetime import date
        for record in self:
            if record.fecha_nac:
                record.edad = date.today().year - record.fecha_nac.year
            else:
                record.edad = 0

    @api.constrains('tipo_pac', 'numero_empleado')
    def _check_numero_empleado(self):
        """Valida que 'numero_empleado' sea obligatorio para los tipos específicos de paciente."""
        for record in self:
            if record.tipo_pac in ['docente', 'personal administrativo', 'personal de servicio'] and not record.numero_empleado:
                raise exceptions.ValidationError(
                    "Debe proporcionar el número de empleado si el tipo de paciente es Docente, Personal Administrativo o Personal de Servicio."
                )

    @api.constrains('numero_cuenta')
    def _check_unique_numero_cuenta(self):
        """Valida que el número de cuenta sea único."""
        for record in self:
            existing = self.search([('numero_cuenta', '=', record.numero_cuenta), ('id', '!=', record.id)])
            if existing:
                raise exceptions.ValidationError("Este número de cuenta ya está en uso.")

    def unlink(self):
        """Evita la duplicación del número de cuenta al eliminar registros."""
        for record in self:
            if record.tipo_pac:
                raise exceptions.UserError("No se pueden eliminar pacientes. La operación está restringida.")
        return super(Paciente, self).unlink()




