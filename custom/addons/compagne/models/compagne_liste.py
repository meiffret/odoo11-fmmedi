
from odoo import models, fields, api

class compagne_liste(models.TransientModel):
    _name = 'compagne.liste'

    name = fields.Char()
    date = fields.Datetime('Date')
    user_id = fields.Many2one('res.users', 'Responsable')
    project_id = fields.Many2one('project.project', 'Affaire')
    opportunite_id = fields.Many2one('crm.lead', 'Opportunité')

    @api.model
    def get_default_statut(self):
        default_statut = 'sansretour'
        return default_statut

    statut = fields.Selection(selection=[('sansretour', 'Sans retour'), ('interesse', 'Intéressé'), ('valide', 'Validé')], default=get_default_statut)

    @api.multi
    def new_compagne_contact_list(self):

        partner = self.env['res.partner']
        if 'active_ids' in self._context:
            partner_ids = self._context['active_ids']

            vals = {'name': self.name,
                    'date': self.date,
                    'user_id': self.user_id.id,
                    'project_id': self.project_id.id,
                    'statut': self.statut,
                    }

            compagne_ids = partner.create_compagne_contact_list(partner_ids, vals)

        return {'type': 'ir.actions.act_window',
                'name': 'liste selectionnée',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'compagne.compagne',
                'res_id': compagne_ids,
                'domain': [('id', 'in', compagne_ids)],
                'target': 'current',
        }



