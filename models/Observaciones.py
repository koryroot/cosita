# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Comments(models.Model):
    _name = 'Comments'
    _description = 'Comments'

    Subject = fields.Char(required=True)
    Msg = fields.Char(required=False)