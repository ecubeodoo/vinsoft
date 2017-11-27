# -*- coding: utf-8 -*- 
from odoo import models, fields, api

class DefaultTheme(models.Model):
	_inherit = 'res.users'

	theme_id = fields.Many2one('color.theme',required=True, default=2,string="Theme")
