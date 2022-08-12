# -*- coding: utf-8 -*-

from odoo import models, fields, api

class References(models.Model):
    _name = 'References'
    _description = 'References'

    PORefDate = fields.Char(required=False)
    PORef = fields.Char(required=True)
    #Subject = fields.Char(required=True) campos condicionales
  