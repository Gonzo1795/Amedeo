from odoo import models,fields,api
class Vehicle_contact(models.Model):
    _inherit = 'res.partner'
    vehicle_ids = fields.One2many(
        comodel_name='vehicle.vehicle',
        inverse_name='res_partner_id',
        string= "Partner"
    )

