# -*- coding: utf-8 -*-
# from odoo import http


# class ShippingLine(http.Controller):
#     @http.route('/shipping_line/shipping_line/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shipping_line/shipping_line/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shipping_line.listing', {
#             'root': '/shipping_line/shipping_line',
#             'objects': http.request.env['shipping_line.shipping_line'].search([]),
#         })

#     @http.route('/shipping_line/shipping_line/objects/<model("shipping_line.shipping_line"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shipping_line.object', {
#             'object': obj
#         })
