from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    date_of_joining = fields.Date(string="Date of Joining", required=True)
    skills_name = fields.Char(string="Skills/Area")
    project_name = fields.Char(string='Project Name')
    project_name1 = fields.Char(string='Second Project Name')
    project_start_date = fields.Date(string='Project Start Date')
    project_start_date1 = fields.Date(string='Second Project Start Date')
    project_end_date = fields.Date(string='Project End Date')
    project_end_date1 = fields.Date(string='Second Project End Date')
    hr_poc = fields.Char(string='HR POC')
    pm = fields.Char(string='PM')
    ppm = fields.Char(string='PPM')
    buddy = fields.Char(string="Buddy")
    experience = fields.Float(string='Experience When Joining')
    total_experience = fields.Float(string="Total Experience", compute='_compute_total_experience', store=True)
    mentor_ids = fields.Many2many('hr.employee', 'employee_mentor_rel', 'employee_id', 'mentor_id', string='Mentors')
    mentee_ids = fields.Many2many('hr.employee', 'employee_mentee_rel', 'employee_id', 'mentee_id', string='Mentees')
    second_email = fields.Char(string='Secondary Email', widget='email', default='someone@example.com', store=True, readonly=False)
    

    project_status = fields.Selection([('main', 'Main'), ('shadow', 'Shadow')], string='Project Status', default='main')
    project_status1 = fields.Selection([('main', 'Main'), ('shadow', 'Shadow')], string='Second Project Status', default='main')

    @api.depends('experience', 'date_of_joining')
    def _compute_total_experience(self):
        for employee in self:
            if employee.experience and employee.date_of_joining:
                days_since_joining = (fields.Date.today() - employee.date_of_joining).days
                years_since_joining = days_since_joining / 365.0
                total_experience = employee.experience + years_since_joining
                employee.total_experience = round(total_experience, 2)
                
    @api.constrains('project_start_date', 'project_end_date')
    def _check_project_dates(self):
        for employee in self:
            if employee.project_start_date and employee.project_end_date and \
                employee.project_end_date < employee.project_start_date:
                raise ValidationError(" Project's start date must precede its end date ")
            
    @api.constrains('project_start_date1', 'project_end_date1')
    def _check_secondary_project_dates(self):
        for employee in self:
            if employee.project_start_date1 and employee.project_end_date1 and \
                employee.project_end_date1 < employee.project_start_date1:
                raise ValidationError(" Project's start date must precede its end date ")
            



