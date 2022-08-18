# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Client(models.Model):
    _name = 'client.client'
    _description = 'client'
    
    SupplierClientID = fields.Char(string = 'Código del cliente ',required=False)
    CIF = fields.Char(string = 'RNC del cliente',required=True)
    Company = fields.Char(string = 'Razón social del cliente',required=True)
    Address = fields.Char(string = 'Domicilio del cliente',required=True)
    City = fields.Char(string = 'Población del cliente',required=True)
    PC = fields.Char(string = 'Código postal del cliente',required=True)
    Province = fields.Char(string = 'Provincia del cliente',required=True)
    Country = fields.Char(string = 'País del cliente en formato ISO3 (DOP)',required=True)
    Email = fields.Char(string = 'Dirección de email del cliente',required=True)





