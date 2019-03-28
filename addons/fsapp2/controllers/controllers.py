# -*- coding: utf-8 -*-
from odoo import http

# class Fsapp2(http.Controller):
#     @http.route('/fsapp2/fsapp2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fsapp2/fsapp2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fsapp2.listing', {
#             'root': '/fsapp2/fsapp2',
#             'objects': http.request.env['fsapp2.fsapp2'].search([]),
#         })

#     @http.route('/fsapp2/fsapp2/objects/<model("fsapp2.fsapp2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fsapp2.object', {
#             'object': obj
#         })