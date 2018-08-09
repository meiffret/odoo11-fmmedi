from odoo import api, fields, models


class warning_wizard(models.TransientModel):
    _name = 'warning.wizard'

    message = fields.Text(string="Plusieurs opportunités sont crées pour un même client et une même campagne", readonly=True, store=True)

    @api.model
    def _test(self,opportunite):

        return {'type': 'ir.actions.act_window',
                'name': 'compagne.warning.wizard',
                'res_model': 'warning.wizard',
                'view_id':'	compagne.view_compagne_warning_wizard',
                'view_mode':'form',
                'view_type':'form',
                'target':'current',
        }