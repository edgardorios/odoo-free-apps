from odoo import fields, models, api
#import logging
#
#_logger = logging.getLogger(__name__)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    banner_text = fields.Char(
        string='Banner Text',
        config_parameter='ribbon_banner.banner_text',
        default='DEV',
        help='Use text to indicate environment (e.g., DEV)'
    )
    banner_text_color = fields.Char(
        string='Banner Text Color',
        config_parameter='ribbon_banner.banner_text_color',
        default='#FFFFFF',
        help='Use HEX color code for text'
    )
    banner_opacity = fields.Float(
        string='Banner Opacity',
        config_parameter='ribbon_banner.banner_opacity',
        default=0.5,
        help='Set opacity between 0.0 (fully transparent) and 1.0 (fully opaque)'
    )
    banner_color = fields.Char(
        string='Banner Background Color',
        config_parameter='ribbon_banner.banner_color',
        default='#FF0000',
        help='Use HEX color code for banner background'
    )
    show_ribbon_banner = fields.Boolean(compute='_compute_show_ribbon_banner')

    def _compute_show_ribbon_banner(self):
        for record in self:
            # Check context for settings module, default to True for General Settings
            module_key = self.env.context.get('module', False)
            #_logger.debug("Computing show_ribbon_banner: module_key=%s", module_key)
            record.show_ribbon_banner = module_key in ('base', 'base_setup', False)

    def set_values(self):
        #_logger.info("Saving Ribbon Banner settings")
        super().set_values()

    @api.model
    def get_values(self):
        #_logger.info("Fetching Ribbon Banner settings")
        res = super().get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update(
            banner_text=ICPSudo.get_param('ribbon_banner.banner_text', 'DEV'),
            banner_color=ICPSudo.get_param('ribbon_banner.banner_color', '#FF0000'),
            banner_text_color=ICPSudo.get_param('ribbon_banner.banner_text_color', '#FFFFFF'),
            banner_opacity=float(ICPSudo.get_param('ribbon_banner.banner_opacity', '0.5')),
        )
        return res
