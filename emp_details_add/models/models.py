from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    skills_name = fields.Char(string="Skills/Area")
    project_name = fields.Char(string='Project Name')
    project_start_date = fields.Date(string='Project Start Date')
    project_end_date = fields.Date(string='Project End Date')
    hr_poc = fields.Char(string='HR POC')
    pm = fields.Char(string='PM')
    ppm = fields.Char(string='PPM')
    experience = fields.Float(string='Experience When Joining')
