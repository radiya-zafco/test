# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Zafco Translate Excel Report',
    'version': '1.0.0',
    'category': 'Translate Excel Report',
    'sequence': -100,
    'summary': 'Zafco Translate Excel Report',
    'description': """Translate excel report from russian language to english language.""",
    'depends': ['web', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/zf_prisma.xml',
        'views/zf_prisma_data.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'external_dependencies': {
        'python': ['openpyxl', 'translate'],
    },
}
