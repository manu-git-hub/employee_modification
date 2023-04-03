from odoo import models, fields, api
from datetime import datetime

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    date_of_joining = fields.Date(string="Date of Joining", required=True)
    skills_name = fields.Char(string="Skills/Area")
    project_name = fields.Char(string='Project Name')
    project_start_date = fields.Date(string='Project Start Date', required=True)
    project_end_date = fields.Date(string='Project End Date', required=True)
    hr_poc = fields.Char(string='HR POC')
    pm = fields.Char(string='PM')
    ppm = fields.Char(string='PPM')
    experience = fields.Float(string='Experience When Joining')
    total_experience = fields.Float(string="Total Experience", compute='_compute_total_experience', store=True)
    mentor_ids = fields.Many2many('hr.employee', 'employee_mentor_rel', 'employee_id', 'mentor_id', string='Mentors')
    mentee_ids = fields.Many2many('hr.employee', 'employee_mentee_rel', 'employee_id', 'mentee_id', string='Mentees')

    @api.depends('experience', 'date_of_joining')
    def _compute_total_experience(self):
        for employee in self:
            if employee.experience and employee.date_of_joining:
                days_since_joining = (fields.Date.today() - employee.date_of_joining).days
                years_since_joining = days_since_joining / 365.0
                total_experience = employee.experience + years_since_joining
                employee.total_experience = round(total_experience, 2)
