from odoo import fields, models

class Page(models.Model):
    _inherit = 'website.page'

    custom_code_head = fields.Html('Custom <head> code', sanitize=False)
    custom_code_footer = fields.Html('Custom end of <body> code', sanitize=False)