from odoo import models, fields, api, _

class Disciple(models.Model):
    _name = 'hogy.disciple'
    _inherit = 'hogy.person'

    coach_id = fields.Many2one('hogy.coach')