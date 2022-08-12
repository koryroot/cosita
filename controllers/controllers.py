# -*- coding: utf-8 -*-
# from odoo import http


# class FacturacionDgii(http.Controller):
#     @http.route('/facturacion_dgii/facturacion_dgii/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facturacion_dgii/facturacion_dgii/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('facturacion_dgii.listing', {
#             'root': '/facturacion_dgii/facturacion_dgii',
#             'objects': http.request.env['facturacion_dgii.facturacion_dgii'].search([]),
#         })

#     @http.route('/facturacion_dgii/facturacion_dgii/objects/<model("facturacion_dgii.facturacion_dgii"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facturacion_dgii.object', {
#             'object': obj
#         })
