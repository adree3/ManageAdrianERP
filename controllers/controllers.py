# -*- coding: utf-8 -*-
# from odoo import http


# class Manageadrian(http.Controller):
#     @http.route('/manageadrian/manageadrian', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manageadrian/manageadrian/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manageadrian.listing', {
#             'root': '/manageadrian/manageadrian',
#             'objects': http.request.env['manageadrian.manageadrian'].search([]),
#         })

#     @http.route('/manageadrian/manageadrian/objects/<model("manageadrian.manageadrian"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manageadrian.object', {
#             'object': obj
#         })
