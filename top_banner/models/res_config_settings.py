from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    top_banner_enabled = fields.Boolean(
        string="Enable Top Banner",
        config_parameter='top_banner.enabled'
    )
    top_banner_text_line1 = fields.Char(
        string="Banner Text Line 1",
        config_parameter='top_banner.text_line1',
        default="Text"
    )
    top_banner_link_line1 = fields.Char(
        string="Banner Link Line 1",
        config_parameter='top_banner.link_line1'
    )
    top_banner_link_text_line1 = fields.Char(
        string="Link Text Line 1",
        config_parameter='top_banner.link_text_line1'
    )
    top_banner_text_color_line1 = fields.Char(
        string="Text Color Line 1",
        config_parameter='top_banner.text_color_line1',
        default="#FFFFFF"
    )
    top_banner_link_color_line1 = fields.Char(
        string="Link Color Line 1",
        config_parameter='top_banner.link_color_line1',
        default="#F9F06B"
    )
    top_banner_color_line1 = fields.Char(
        string="Background Color Line 1",
        config_parameter='top_banner.color_line1',
        default="#1A5FB4"
    )
    top_banner_text_line2 = fields.Char(
        string="Banner Text Line 2",
        config_parameter='top_banner.text_line2'
    )
    top_banner_link_line2 = fields.Char(
        string="Banner Link Line 2",
        config_parameter='top_banner.link_line2'
    )
    top_banner_link_text_line2 = fields.Char(
        string="Link Text Line 2",
        config_parameter='top_banner.link_text_line2'
    )
    top_banner_text_color_line2 = fields.Char(
        string="Text Color Line 2",
        config_parameter='top_banner.text_color_line2',
        default="#FFFFFF"
    )
    top_banner_link_color_line2 = fields.Char(
        string="Link Color Line 2",
        config_parameter='top_banner.link_color_line2',
        default="#F9F06B"
    )
    top_banner_color_line2 = fields.Char(
        string="Background Color Line 2",
        config_parameter='top_banner.color_line2',
        default="#1A5FB4"
    )
    link_type_line1 = fields.Selection(
        [('text', 'Text Link'), ('button', 'Button Link')],
        string="Link Type Line 1",
        config_parameter='top_banner.link_type_line1',
        required=True,
        default='text'
    )
    button_color_line1 = fields.Char(
        string="Button Color Line 1",
        config_parameter='top_banner.button_color_line1',
        default="#E01B24"
    )
    link_type_line2 = fields.Selection(
        [('text', 'Text Link'), ('button', 'Button Link')],
        string="Link Type Line 2",
        config_parameter='top_banner.link_type_line2',
        required=True,
        default='text'
    )
    button_color_line2 = fields.Char(
        string="Button Color Line 2",
        config_parameter='top_banner.button_color_line2',
        default="#E01B24"
    )