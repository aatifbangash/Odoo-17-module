from odoo import models, fields, api


class school(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    name = fields.Char()
    description = fields.Text()
