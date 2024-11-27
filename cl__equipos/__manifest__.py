{
    'name': 'Gestión de Equipos',
    'version': '1.0',
    'author': 'Joasro',
    'category': 'Healthcare',
    'summary': 'Gestión de equipos en una clínica',
    'description': """
    Módulo para la gestión de equipos, permitiendo agregar, actualizar y consultar inventarios.
    """,
    'depends': ['base'],  # Agrega dependencias necesarias
    'data': [
        'security/ir.model.access.csv',  # Archivo de permisos
        'views/equipo.xml',  # Vistas de medicamentos
        'views/menu.xml',  # Menú principal (si es necesario)
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

