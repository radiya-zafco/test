# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ZafcoPrismaDatas(models.Model):
    _name = "zf.prisma.data"
    _description = "zf prisma data excel report"
    _rec_name = 'destination_data'

    source_data=fields.Text(string="Source Data")
    destination_data=fields.Text(string="Destination Data")
    source_lang=fields.Text(string="Source Language", default="Russian")
    destination_lang=fields.Text(string="destination Language",default="English")