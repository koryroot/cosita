# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Supplier(models.Model):
    _name = 'supplier'
    _description = 'supplier'

    
    SupplierID = fields.Char()
    CIF = fields.Char(required=True)
    Company = fields.Char(required=True)
    Address = fields.Char(required=True)
    City = fields.Char(required=True)
    PC = fields.Char(required=True)
    Province = fields.Char(required=True)
    Country = fields.Char(required=True)
    Email = fields.Char(required=True)


     

