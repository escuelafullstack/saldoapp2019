# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class prueb_addon2(models.Model):
#     _name = 'prueb_addon2.prueb_addon2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100