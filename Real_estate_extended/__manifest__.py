{
    'name' : 'Real Estate Extended',
    'version' : '1.0',
    'summary': 'Real Estate Extended',
    'depends' : [
        'mail',
        'Real_estate',
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_menu.xml',
        'views/estate_property_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}