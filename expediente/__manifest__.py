# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Expedientes',
    'version': '1.0',
    'summary': 'Gestión de pacientes en la clínica',
    'author': 'Angel',
    'category': 'Medical',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/inicio.xml',
        'views/paciente.xml',
        'views/formulario_cita.xml',
        'views/lista_cita.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}


