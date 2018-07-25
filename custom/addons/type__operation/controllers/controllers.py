# -*- coding: utf-8 -*-
from odoo import http

# class TypeOperation(http.Controller):
#     @http.route('/type__operation/type__operation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/type__operation/type__operation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('type__operation.listing', {
#             'root': '/type__operation/type__operation',
#             'objects': http.request.env['type__operation.type__operation'].search([]),
#         })

#     @http.route('/type__operation/type__operation/objects/<model("type__operation.type__operation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('type__operation.object', {
#             'object': obj
#         })