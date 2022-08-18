# -*- coding: utf-8 -*-

from dataclasses import field
import string
from odoo import models, fields, api

class GeneralData(models.Model):
    _name = 'generaldata'
    _description = 'GeneralData'

    Ref = fields.Char(string = 'Numero de documento',required=True)
    Type = fields.Selection([('FacturaComercial'),('FacturaConsumo'),('FacturaAbono'),('FacturaDebito'),('FacturaProveedorInformal'),('FacturaGastosMenores'),('RegimenEspecial'),('GubernamentalDOM')],required=True)
    Date = fields.Date(string='',required=True) #formato AAAA-MM-DD
    Currency = fields.Char(string = 'Moneda',required=True) #verificar si es un campo selection
    NCF = fields.Char(string= 'Número de Comprobante Fiscal',required=True)
    NCFExpirationDate = fields.Char(required=True)
    BeginDate = fields.Char(required=False)
    EndDate = fields.Char(required=False) #verificar por que es char y no date
    TaxIncluded = fields.Boolean(required=True)
    CAS =  fields.Integer(required=True)
    ExchangeRate = fields.Float(required=True)

class PublicAdministration(models.Model):
    _name = ''
    _description = ''

    TipoIngreso = fields.Char(required=True) #verificar si estos campos no van en selection
    TipoPago = fields.Char(required=True)
    LinesPerPrintedPage = fields.Char(required=True)
    










    





