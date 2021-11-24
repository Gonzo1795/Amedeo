# Copyright 2021-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models,fields,api


class Vehicle(models.Model):
    _name = 'vehicle.vehicle'
    _description = "Vehicle Model"

    name = fields.Char(
        string="Name",
        required=True,
    )
    vehicle_type = fields.Selection(
        selection=[
            ("bike","bike"),
            ("car","car"),
            ("van","van"),
        ],
        string="vehicle type",
    )
    daily_fare = fields.Float(
        string="daily fare ",
        compute="_compute_daily_fare",
        store=True,
    )
    color = fields.Integer()



    year_of_registration = fields.Integer(
        string="year_of_registration",
        
    )
    res_partner_id = fields.Many2one(
        comodel_name= 'res.partner',
        string = "holder",
    )
    license_plate=fields.Char(
        string= "license_plate",
    )
    #_sql_constraints = [("license_plate_unique", "UNIQUE(license_plate)", "Warning: license plate already exists!")]

    garage_id = fields.Many2one(
        comodel_name='garage.garage',
        string="Garage"
    )
    @api.depends("vehicle_type")
    def _compute_daily_fare(self):
        if self.vehicle_type == "bike":
            self.daily_fare= 5
        elif self.vehicle_type == "car":
            self.daily_fare = 10
        elif self.daily_fare=="van":
            self.daily_fare = 15

    @api.model
    def create(self,values):
        if "license_plate" in values.keys():
            if values ["license_plate"]:
                values["license_plate"]=values["license_plate"].upper()
                
        Schedule= {'name':'Contact_copy'}
        holder = self.env['res.partner'].create(Schedule)
        values["res_partner_id"]= holder.id

        return super (Vehicle,self).create (values)

    def write(self,values):
        if "license_plate" in values.keys():
            values["license_plate"]=values["license_plate"].upper()
        return super (Vehicle,self).write (values)

