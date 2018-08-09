
from odoo import models, fields, api

class crm_lead(models.Model):

    _inherit="crm.lead"



    # compagne_id = fields.Many2one('compagne.compagne','Compagne')
    # partner_id = fields.Many2one('crm.lead')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            return {'domain': {'compagne_id': [('partner_id', '=', self.partner_id.id)]}}
        else:
            return {'domain': {'compagne_id': []}}