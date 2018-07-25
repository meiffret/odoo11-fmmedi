# -*- coding: utf-8 -*-
from odoo import http

# class Compagne(http.Controller):
#     @http.route('/compagne/compagne/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compagne/compagne/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('compagne.listing', {
#             'root': '/compagne/compagne',
#             'objects': http.request.env['compagne.compagne'].search([]),
#         })

#     @http.route('/compagne/compagne/objects/<model("compagne.compagne"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compagne.object', {
#             'object': obj
#         })