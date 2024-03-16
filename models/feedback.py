from odoo import fields, models, api
from odoo.exceptions import ValidationError


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
                   ], string="Rating", default='0', required=1)
    removed_activity = fields.Boolean(string="Removed Activity", default=False)
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], string='Status', default='draft', tracking=True)

    # @api.model
    # def create(self, vals):
    #     print(vals)
    #     self.activity_schedule(
    #         'directors_feedback.mail_activity_for_directors_feedback', user_id=self.employee_id.user_id.id,
    #         note=f'Your have a feedback from director side'),
    #
    #     return super(DirectorsFeedback, self).create(vals)

    def action_sent_activity(self):
        if self.rating == '0':
            raise ValidationError('Please Select Rating')
        else:
            self.activity_schedule(
                'directors_feedback.mail_activity_for_directors_feedback', user_id=self.employee_id.user_id.id,
                note=f'Your have a feedback from director side')
            print('action sent activity')
            self.state = 'done'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Your feedback has been sent.',
                    'type': 'rainbow_man',
                }
            }


    def action_remove_activity(self):
        activity_id = self.env['mail.activity'].search(
            [ ('user_id', '=', self.employee_id.user_id.id), (
                'activity_type_id', '=', self.env.ref('directors_feedback.mail_activity_for_directors_feedback').id)])
        if activity_id:
            activity_id.sudo().action_feedback(feedback=f'Done..')
        self.sudo().removed_activity = True

