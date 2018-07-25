# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _

class compagne(models.Model):
    _name = 'compagne.compagne'

    name = fields.Char()
    partner_id = fields.Many2one('res.partner', 'Contact')
    user_id = fields.Many2one('res.users', 'Responsable')
    task_id = fields.Many2one('project.task', 'Sous_affaire')
    project_id = fields.Many2one('project.project', 'Affaire')
    opportunite_id = fields.Many2one('crm.lead', 'Opportunité')
    statut = fields.Selection([('sansretour', 'Sans retour'), ('interesse', 'Intéressé'), ('valide', 'Validé'), ('nonvalide', 'Non Validé')])
    ville = fields.Char(related='partner_id.city')
    departement = fields.Char()
    code_postal = fields.Char(related='partner_id.zip')
    date = fields.Datetime('Date')
    description = fields.Text()
    on_change = fields.Boolean(default=False)

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

    # @api.model
    # def _onchange_stage_values(self, opportunite_id):
    #     # if not opportunite_id:
    #     #     return False
    #     opportunite = self.env['crm.lead'].browse(opportunite_id)
    #     # if opportunite.stage_id != 4:
    #     #     self.on_change = False
    #     if opportunite_id == 7:
    #         self.on_change = True

    @api.onchange('opportunite_id')
    def _onchange_statut_valid(self):
        # if not self.opportunite_id:
        #     self.statut = 'sansretour'
        if self.opportunite_id != '7':
            self.on_change = True
            self.statut = 'valide'

    # @api.onchange('on_change')
    # def _onchange_statut_valid(self):
    #     if self.on_change == True:
    #         self.statut = 'valide'

    #
    # @api.onchange('opportunite_id')
    # def _onchange_statut(self):
    #     if self.opportunite_id:
    #         self.statut = 'interesse'