{
    'name': 'Medical Partner',
    'version': '1.0',
    'summary': 'Gestión de Pacientes y Citas Médicas',
    'author': 'Tu Nombre',
    'category': 'Medical',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/paciente.xml',
        'views/inicio.xml',
        'views/formulario_cita.xml',
        'views/lista_cita.xml',
    ],
    'installable': True,
    'application': True,
}
