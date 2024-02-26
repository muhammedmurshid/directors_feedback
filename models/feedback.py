from odoo import fields, models, api


class DirectorsFeedback(models.Model):
    _name = 'directors.feedback'
    _description = 'Director Feedback'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string="Employee Name", required=1)
    feedback = fields.Text(string="Feedback")
    date = fields.Date(string="Date", default=fields.Date.today)
    rating = fields.Selection(
        selection=[('0', 'No rating'), ('1', 'Bad'), ('2', 'Medium'), ('3', 'Good'),
                   ], string="Rating", default='0')
