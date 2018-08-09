# -*- coding: utf-8 -*-


from odoo import api, fields, models, tools, exceptions, _

class compagne(models.Model):
    _name = 'compagne.compagne'

    @api.one
    @api.depends('historique')
    def _compute_historic(self):
        if self.task_id:
            self.historique = str(self.date) + '  '+ str ('Affaire: ') + str(self.project_id.name) + ' / '+ str(self.task_id.name)+  '   '  + str('Campagne: ').__sizeof__(16) + str(self.name)  + '--' + str(self.statut)
        else:
            self.historique = str(self.date) + '  ' + str('Affaire: ') + str(self.project_id.name)  + '   ' + str('Campagne: ') + str(self.name) + '--' + str(self.statut)

    name = fields.Char()
    historique = fields.Text(compute='_compute_historic')
    partner_id = fields.Many2one('res.partner', 'Contact')
    user_id = fields.Many2one('res.users', 'Responsable')
    task_id = fields.Many2one('project.task', 'Sous_affaire')
    project_id = fields.Many2one('project.project', 'Affaire')
    opportunity= fields.Char()
    statut_id = fields.Integer(string="Stage")
    statut = fields.Char(compute="_onchange_stage")
    ville = fields.Char(related='partner_id.city')
    departement = fields.Char()
    code_postal = fields.Char(related='partner_id.zip')
    date = fields.Date('Date')
    description = fields.Text()
    gagne = fields.Boolean(default=False)
    # compa = fields.Many2one('compagne.compagne', related='partner_id.opportunity_ids.compagne_id')
    # compa_compa = fields.Char()
    # on_change = fields.Boolean(default=False)
    # partner_opp_count = fields.Integer(related='partner_id.opportunity_count')

    # oppot_part_id = fields.Many2one('crm.stage','stage',related='opportunite_id.stage_id')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

    @api.model
    def _compare_compagne_partner(self, partner_id):
        partner = self.env['res.partner'].browse(partner_id)
        opportunite = partner.env['crm.lead'].search([('compagne_id','=',self.id),('partner_id','=',self.partner_id.id)])
        opportunite_count = partner.env['crm.lead'].search_count([('compagne_id', '=', self.id), ('partner_id', '=', self.partner_id.id)])

        if opportunite_count <= 1:
            order = opportunite.env['sale.order'].browse(opportunite.order_ids)
            order_count = order.search_count([('opportunity_id', '=', opportunite.id)])
            if ((order != False) & (order_count != 0))&(opportunite_count != 0):
                for ord in order:
                    order_count = ord.search_count([('opportunity_id','=',opportunite.id)])
                 # order = opportunite.env['sale.order'].search([('id','=',opportunite.order_ids.id)])

                    if opportunite_count == 1:
                        opp = opportunite.name
                        self.opportunity = opp
                        state = opportunite.stage_id.id
                        if state == 4:
                            self.gagne = True
                        else:
                            self.gagne = False
                        return opportunite,order_count
                    # print('Plusieurs opportunités sont crées pour un même client et une même campagne ')
            else:
                return opportunite, False
        else:
            # wiz=self.env['warning.wizard']
            # wiz._test()
            # exceptions.Warning('Plusieurs opportunités sont crées pour un même client et une même campagne')
            self.statut = 'Erreur : Plusieurs opportunités sont crées pour un même client et une même campagne'
            return False,False
    # wt = self.env['model.name']
    # id_needed = wt.search([('field1', '=', 'value')]).id
    # new = wt.browse(id_needed)
    # list = [new.field1, new.field2, new.field3]

    @api.one
    def _onchange_stage(self):
        for compagne in self:
            test = self.partner_id.id
            value,devis = compagne._compare_compagne_partner(self.partner_id)
            if value:
                compagne.statut = 'Intéressé'
                if devis:
                    if devis != 0 :
                        compagne.statut = 'Devis crée'
                        if compagne.gagne == True:
                            compagne.statut = 'Devis validé/ Gagné'
            # else:
            #     compagne.statut = 'Sans retour'

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        if self.env.context.get('partner_id'):
            args = args + [('partner_id', '=', self.env.context.get('partner_id'))]
        firsts_records = self.search([('partner_id', '=ilike', name)] + args, limit=limit)
        search_domain = [('name', operator, name)]
        search_domain.append(('id', 'not in', firsts_records.ids))
        records = firsts_records + self.search(search_domain + args, limit=limit)
        return [(record.id, record.display_name) for record in records]


    # @api.multi
    # def _opp_verif(self):
    #     partner = self.env['res.partner']
    #     name_computed = self.name
    #     value = partner._compare_opportunity_compagne(name_computed)
    #     self.statut = value
    #     return value



# if self.statut_id==4:
        #     self.statut= 'Validé'
        # elif self.statut_id==3:
        #     self.statut= 'Intéressé'
        # elif self.statut_id==2:
        #     self.statut= 'Intéressé'
        # elif self.statut_id==1:
        #     self.statut= 'Intéressé'
        # else:
        #     self.statut= 'Sans retour'

    #
    # @api.model
    # def _onchange_stage_values(self, opportunite_id):
    #     if not opportunite_id:
    #         return {}
    #     opportunite = self.env['crm.lead'].browse(opportunite_id)
    #     self.name = opportunite.name
    #     if opportunite.name:
    #         self.on_change = True
    #         return {
    #             'stage': opportunite.stage_id
    #         }
    #
    #
    # @api.onchange('opportunite_id')
    # def _onchange_statut_valid(self):
    #
    #     values = self._onchange_stage_values(self.opportunite_id.id)
    #     self.update(values)
    #     if self.opportunite_id:
    #         self.statut_id = 'interesse'
    #         if self.stage == 4:
    #             self.statut_id = 'valide'
    #
    # @api.onchange('opportunity_count')
    # def _onchange_partner(self):
    #
    #
    #     value = self._onchange_partner_opp(self.partner_id.id)
    #     self.update(value)

    # @api.model
    # def _onchange_partner_opp(self, partner_id):
    #
    #     partner = self.env['res.partner'].browse(partner_id)
    #
    #     if self.partner_opp_count == 1:
    #         # opp= partner.env['crm.lead'].browse(opportunity_ids)
    #         # if opp.compagne_id == self.name:
    #         #     self.opportunite_id = opp
    #         #     return True
    #         opportunit = partner.opportunity_ids
    #         return { 'opportunite_id':opportunit, }
    #         self.opportunite_id = partner.opportunity_ids
    #     return {}
    #
    #
    # @api.onchange('partner_id')
    # def _onchange_partner(self):
    #
    #     value = self._onchange_partner_opp(self.partner_id.id)
    #     self.update(value)