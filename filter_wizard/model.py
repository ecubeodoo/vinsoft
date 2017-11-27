# -*- coding: utf-8 -*- 
from odoo import models, fields, api

class FilterWizard(models.Model):
	_name = "filters.wizard"

	form = fields.Date(string="Fecha Desde")
	to = fields.Date(string="Fecha Hasta") 

	@api.multi
	def get_result(self):
		return {
		'type': 'ir.actions.act_window',
		'name': 'Fecha sabia resultados',
		'res_model': 'account.move.line',
		'view_type': 'form',
		'view_mode': 'tree,form',
		'context': {},
		'domain': ([('date','>=',self.form),('date','<=',self.to)]),
		}

class FilterAccountMoveLine(models.Model):
	_inherit = "account.move.line"    
