# -*- coding: utf-8 -*-
from odoo import http

# class DanielMoreno(http.Controller):
#     @http.route('/daniel_moreno/daniel_moreno/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/daniel_moreno/daniel_moreno/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('daniel_moreno.listing', {
#             'root': '/daniel_moreno/daniel_moreno',
#             'objects': http.request.env['daniel_moreno.daniel_moreno'].search([]),
#         })

#     @http.route('/daniel_moreno/daniel_moreno/objects/<model("daniel_moreno.daniel_moreno"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('daniel_moreno.object', {
#             'object': obj
#         })