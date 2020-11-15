from odoo import models, fields, api, _

class Person(models.Model):
    _name = 'hogy.person'

    name = fields.Char(string=_("Name"))
    birth_date = fields.Date(string=_("Birth date"))
    email = fields.Char(string="Email")
    user_id = fields.Many2one('res.users', string=_("User account"))

    def __str__(self):
        return "Person(name="+self.name+",birth_date="+self.birth_date+",email="+self.email+",user_id="+self.user_id.id+")"

    def __repr__(self):
        return {
            'name': self.name,
            'birth_date': self.birth_date,
            'email': self.email,
            'user_id': self.user_id.id
        }
