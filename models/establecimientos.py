# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Customers(models.Model):
    _name = 'Customers'
    _description = 'Customers'

    SupplierClientID = fields.Char(required=True)
    SupplierCustomerID = fields.Char(required=False)
    Customer = fields.Char(required=True)
    Address = fields.Char(required=True)
    City = fields.Char(required=True)
    PC  = fields.Char(required=True)
    Province = fields.Char(required=True)
    Country = fields.Char(required=True)

