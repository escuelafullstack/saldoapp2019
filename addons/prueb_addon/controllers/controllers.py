# -*- coding: utf-8 -*-
from odoo import http

# class PruebAddon(http.Controller):
#     @http.route('/prueb_addon/prueb_addon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueb_addon/prueb_addon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueb_addon.listing', {
#             'root': '/prueb_addon/prueb_addon',
#             'objects': http.request.env['prueb_addon.prueb_addon'].search([]),
#         })

#     @http.route('/prueb_addon/prueb_addon/objects/<model("prueb_addon.prueb_addon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueb_addon.object', {
#             'object': obj
#         })