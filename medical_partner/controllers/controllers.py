# -*- coding: utf-8 -*-
# from odoo import http


# class MedicalPartner(http.Controller):
#     @http.route('/medical_partner/medical_partner', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/medical_partner/medical_partner/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('medical_partner.listing', {
#             'root': '/medical_partner/medical_partner',
#             'objects': http.request.env['medical_partner.medical_partner'].search([]),
#         })

#     @http.route('/medical_partner/medical_partner/objects/<model("medical_partner.medical_partner"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('medical_partner.object', {
#             'object': obj
#         })

