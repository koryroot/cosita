# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class facturacion_dgii(models.Model):
#     _name = 'facturacion_dgii.facturacion_dgii'
#     _description = 'facturacion_dgii.facturacion_dgii'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
