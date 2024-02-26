{
    'name': "Directors Feedback",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['mail', 'hr'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/directors_feedback.xml'
    ],
    'demo': [],
    'summary': "directors_feedback_logic",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': True
}
