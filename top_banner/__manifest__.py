{
    'name': "Top Banner",
    'summary': "Add a customizable two-line banner for Odoo screens to communicate important messages",
    'description': """
        Add a customizable two-line banner at the top of Odoo screens. Perfect for displaying environment indicators 
        (e.g., Test, Staging, Production), system maintenance alerts, internal communications, reminders, or support information.
        Features include configurable text, background color, text color, optional hyperlinks, and simple setup via Odoo Settings.
    """,
    'author': "Edgardo Rios",
    'website': 'https://github.com/edgardorios/odoo-free-apps',
    'category': 'Tools',
    'version': '18.0.1.0.0',
    'depends': ['base', 'web'],
    'sequence': 1000,  # High sequence to load last
    'data': [
        'views/top_settings_view.xml',
        'views/web_top_banner.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'top_banner/static/src/css/top_banner.css',
        ],
    },
    'images': [
        'static/description/screenshot1.png',
        'static/description/screenshot2.png',
        'static/description/screenshot3.png',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}