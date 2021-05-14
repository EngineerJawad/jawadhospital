{
    'name' : 'Jawad Hospital Management',
    'version' : '12.0.1.0',
    'summary': 'A Module For Management System',
    'sequence': 10,
    'category': 'Extra Tools',
    'website': 'https://www.youtube.com/channel/UC8_i8IMUXCBY1NPJ6QHzwBA',
    'depends' : ['base','mail','sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/sequence2.xml',
        'views/patient.xml',
        'views/appointment.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}