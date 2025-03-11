{
    'name': "Expediente con res_partner",
    'description': "Res_partner",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/formulario_cita.xml',
        'views/inicio.xml',
        'views/lista_cita.xml',
        'views/menu.xml',
        'views/paciente.xml',
    ],
    'version': '1.0',
    'author': "Joasro",
    'installable': True,
    'application': False,
}