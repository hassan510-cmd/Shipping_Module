# -*- coding: utf-8 -*-
# from odoo import http


# class PanMarine(http.Controller):
#     @http.route('/pan_marine/pan_marine/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pan_marine/pan_marine/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pan_marine.listing', {
#             'root': '/pan_marine/pan_marine',
#             'objects': http.request.env['pan_marine.pan_marine'].search([]),
#         })

#     @http.route('/pan_marine/pan_marine/objects/<model("pan_marine.pan_marine"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pan_marine.object', {
#             'object': obj
#         })

