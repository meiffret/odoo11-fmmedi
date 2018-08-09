
from odoo import models, fields, api

class res_partner(models.Model):
    _inherit="res.partner"


    compagne_id = fields.One2many('compagne.compagne','partner_id','Campagne')

    historique = fields.Text(compute="_compute_historic")


    @api.model
    def _compute_historic(self):
        for partner in self:
            compagne = partner.env['compagne.compagne'].search([('partner_id','=',partner.id)])
            for comp in compagne:
                if partner.historique:
                    partner.historique = str(partner.historique)+ '\n' + comp.historique
                    partner.comment= str(partner.historique)+ '\n' + partner.historique
                else:
                    partner.historique = comp.historique
                    partner.comment = partner.historique

    @api.model
    def create_compagne_contact_list(self, partner_ids, vals):

        compagne_1 = self.env['compagne.compagne']
        compagne_ids = []

        if partner_ids:
            for partner in self.browse(partner_ids):
                new_compagne = compagne_1.create(
                                                    {'name': vals['name'],
                                                     'date': vals['date'],
                                                     'user_id': vals['user_id'],
                                                     'project_id': vals['project_id'],
                                                     'partner_id': partner.id,
                                                     'city': partner.city,
                                                     'zip': partner.zip,
                                                     }
                                                )
                compagne_ids.append(new_compagne.id)
        return compagne_ids



# class compagne(models.Model):
#     _name = 'compagne.compagne'
#
#     # @api.one
#     # @api.depends('partner_id')
#     # def _compute_name(self):
#     #     self.name = str(self.name_computed) + '-' + str(self.partner_id.name)
#
#
#
#     name = fields.Char()
#     # name_computed = fields.Char(compute='_compute_name')
#     partner_id = fields.Many2one('res.partner', 'Contact',required=True)
#     user_id = fields.Many2one('res.users', 'Responsable')
#     task_id = fields.Many2one('project.task', 'Sous_affaire')
#     project_id = fields.Many2one('project.project', 'Affaire')
#     # opportunite_id = fields.One2many('crm.lead', 'partner_id' ,related='partner_id.opportunity_ids')
#     opportunity= fields.Char()
#     # statut_id = fields.Many2one('crm.stage',related='partner_id.opportunity_ids.stage_id', compute='_compare_compagne_partner')
#     statut_id = fields.Integer(string="Stage")
#     statut = fields.Char(compute="_onchange_stage", attr="readOnly")
#     ville = fields.Char(related='partner_id.city')
#     departement = fields.Char()
#     code_postal = fields.Char(related='partner_id.zip')
#     date = fields.Datetime('Date')
#     description = fields.Text()
#
#     @api.model
#     def _compare_compagne_partner(self, partner_id):
#         verif_nom = self.name
#         partner = self.env['res.partner'].browse(partner_id)
#
#         opportunite = partner.env['crm.lead'].search([('compagne_id','=',self.id),('partner_id','=',self.partner_id.id)])
#         opportunite_count = partner.env['crm.lead'].search_count(
#             [('compagne_id', '=', self.id), ('partner_id', '=', self.partner_id.id)])
#         if opportunite_count < 1:
#             try :
#                 self.opportunity = opportunite.name
#                 self.statut_id= opportunite.stage_id
#                 return opportunite
#             except:
#                 print('Plusieurs opportunités sont crées pour un même client et une même compagne ')
#
#     @api.one
#     def _onchange_stage(self):
#
#         for compagne in self:
#             test = self.partner_id.id
#             value = compagne._compare_compagne_partner(self.partner_id)
#             if value:
#                 if not compagne.statut_id:
#                     compagne.statut = 'Sans retour'
#                 if compagne.statut_id == 4:
#                     compagne.statut = 'Validé'
#                 else:
#                     compagne.statut = 'Intéressé'
#
#
#     @api.model
#     def name_search(self, name='', args=None, operator='ilike', limit=100):
#         if args is None:
#             args = []
#         if self.env.context.get('partner_id'):
#             args = args + [('partner_id', '=', self.env.context.get('partner_id'))]
#         firsts_records = self.search([('partner_id', '=ilike', name)] + args, limit=limit)
#         search_domain = [('name', operator, name)]
#         search_domain.append(('id', 'not in', firsts_records.ids))
#         records = firsts_records + self.search(search_domain + args, limit=limit)
#         return [(record.id, record.display_name) for record in records]
