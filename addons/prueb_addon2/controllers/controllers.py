# -*- coding: utf-8 -*-
from odoo import http

# class PruebAddon2(http.Controller):
#     @http.route('/prueb_addon2/prueb_addon2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueb_addon2/prueb_addon2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueb_addon2.listing', {
#             'root': '/prueb_addon2/prueb_addon2',
#             'objects': http.request.env['prueb_addon2.prueb_addon2'].search([]),
#         })

#     @http.route('/prueb_addon2/prueb_addon2/objects/<model("prueb_addon2.prueb_addon2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueb_addon2.object', {
#             'object': obj
#         })