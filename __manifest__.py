{
    'name': "School Management",
    'summery': "School Management Software",
    'description': "Treating Schools",
    'author': "Bappi Saha",
    'category': "Tools",
    'versions': "16.0.1",
    'depends': ['base', 'contacts', 'hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/school.xml'
    ],
    'sequence': 0,
    "installable": True,
    'application': True,
}