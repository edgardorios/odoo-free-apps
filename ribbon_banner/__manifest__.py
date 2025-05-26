{
    'name': 'Ribbon Banner',
    'version': '18.0.3.0.0',
    'category': 'Tools',
    'summary': 'Add a customizable ribbon banner to display environment and database name',
    'description': """
        Ribbon Banner adds a customizable ribbon to Odoo, displaying the environment (e.g., DEV, TEST, STAGING) and database name.
        Configure the banner's text, background color, and text color directly in Settings > General Settings.
        Perfect for multi-environment setups to avoid confusion!
    """,
    'author': 'Edgardo Rios',
    'website': 'https://github.com/edgardorios/odoo-free-apps',
    'license': 'LGPL-3',
    'depends': ['base', 'base_setup', 'web'],
    'data': [
        'views/ribbon_settings_view.xml',
        'views/web_ribbon_banner.xml',
    ],
    'images': ['static/description/icon.png'],
    'support': 'edgardo.rios@gmail.com',
    'application': True,
    'installable': True,
    'auto_install': False,
}