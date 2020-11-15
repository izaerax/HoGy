from odoo import models, fields, api, _

class Coach(models.Model):
    _name = 'hogy.coach'
    _inherit = 'hogy.person'

    disciple_ids = fields.One2many('hogy.disciple', inverse_name='coach_id')