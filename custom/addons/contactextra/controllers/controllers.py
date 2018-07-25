# -*- coding: utf-8 -*-
from odoo import http

# class Contactextra(http.Controller):
#     @http.route('/contactextra/contactextra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contactextra/contactextra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contactextra.listing', {
#             'root': '/contactextra/contactextra',
#             'objects': http.request.env['contactextra.contactextra'].search([]),
#         })

#     @http.route('/contactextra/contactextra/objects/<model("contactextra.contactextra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contactextra.object', {
#             'object': obj
#         })