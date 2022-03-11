from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from odoo.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    is_booking_order = fields.Boolean(
        string='Is Booking Order', 
        default=True)

    team = fields.Many2one(
        'service.team', 
        string='Team')

    team_leader = fields.Many2one(
        comodel_name='res.users', 
        string='Team Leader')

    team_members = fields.Many2many(
        comodel_name='res.users', 
        string='Team Members')

    booking_start = fields.Datetime(
        string='Booking Start')
        
    booking_end = fields.Datetime(
        string='Booking End')

    @api.onchange('team')
    def get_team(self):
        for rec in self:
            rec.team_leader = self.team.team_leader
            rec.team_members = self.team.team_members

    def cek_work_order(self):
        work = self.env['work.order'].search([
        '&', ('team_id', '=', self.team.id),
            ('team_members', 'in', self.team_members.ids),
            ('state', 'not in', 'cancel'),
            ('planned_start','=', self.booking_start), 
            ('planned_end','=', self.booking_end),
        ], limit=1)
        if work:
            raise ValidationError("Team already has work order during that period ")
        else:
            raise ValidationError("Team is available for booking.")
        
    