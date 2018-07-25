
from odoo import models, fields, api

class res_partner(models.Model):
    _inherit="res.partner"

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
                                                     'statut': vals['statut'],
                                                     'partner_id': partner.id,
                                                     'city': partner.city,
                                                     'zip': partner.zip,
                                                     }
                                                )
                compagne_ids.append(new_compagne.id)
        return compagne_ids
