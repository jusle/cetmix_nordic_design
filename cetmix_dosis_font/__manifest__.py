# Copyright 2024 Ab Cetmix Nordic Oy
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    'name': 'Cetmix Dosis Font',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Custom Dosis Font for Odoo',
    'description': """
        This module adds the Dosis font to Odoo.
    """,
    'author': 'Cetmix Nordic Ltd.',
    'website': 'http://www.cetmix.fi',
    'depends': ['base'],
    ],
    'assets': {
        'web.assets_frontend': [
            'cetmix_dosis_font/static/src/css/dosis.css',
        ],
        'web.assets_backend': [
            'cetmix_dosis_font/static/src/css/dosis.css',
        ],
        'web.assets_common': [
            'cetmix_dosis_font/static/src/css/dosis.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}