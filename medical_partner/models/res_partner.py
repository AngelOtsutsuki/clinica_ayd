from odoo import models, fields, api, exceptions
from datetime import date

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Campos específicos para paciente
    is_patient = fields.Boolean(string="¿Es paciente?", default=False)
    tipo_pac = fields.Selection([
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
        ('visitante', 'Visitante'),
        ('personal_administrativo', 'Personal Administrativo'),
        ('personal_servicio', 'Personal de Servicio'),
    ], string='Tipo de Paciente')
    numero_empleado = fields.Char(string='Número de Empleado', help="Requerido si es docente o personal")
    numero_cuenta = fields.Char(string='Número de Cuenta', unique=True)
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    ], string='Género')
    fecha_nac = fields.Date(string='Fecha de Nacimiento')
    edad = fields.Integer(string='Edad', compute="_compute_edad", store=True)
    alergias = fields.Text(string='Alergias')
    med_act = fields.Text(string='Medicamentos Actuales')
    enf_pre = fields.Text(string='Enfermedades Preexistentes')
    # Contacto de emergencia
    nombre_cont = fields.Char(string='Nombre del Contacto')
    relacion = fields.Char(string='Relación')
    telefono_cont = fields.Char(string='Número de Teléfono')
    telefono_cont2 = fields.Char(string='Otro Teléfono')
    # Relación con citas médicas
    citas_ids = fields.One2many('expediente.citamedica', 'paciente_id', string='Citas Médicas')

    @api.depends('fecha_nac')
    def _compute_edad(self):
        for record in self:
            if record.fecha_nac:
                today = date.today()
                # Cálculo de edad exacto
                record.edad = today.year - record.fecha_nac.year - ((today.month, today.day) < (record.fecha_nac.month, record.fecha_nac.day))
            else:
                record.edad = 0

    @api.constrains('tipo_pac', 'numero_empleado')
    def _check_numero_empleado(self):
        for record in self:
            if record.is_patient and record.tipo_pac in ['docente', 'personal_administrativo', 'personal_servicio'] and not record.numero_empleado:
                raise exceptions.ValidationError("Debe proporcionar el número de empleado para este tipo de paciente.")

    @api.constrains('numero_cuenta')
    def _check_unique_numero_cuenta(self):
        for record in self:
            if record.numero_cuenta:
                existing = self.search([('numero_cuenta', '=', record.numero_cuenta), ('id', '!=', record.id)])
                if existing:
                    raise exceptions.ValidationError("Este número de cuenta ya está en uso.")
