# Copyright 2021-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models,fields,api
import random


class Garage(models.Model):
    _name = 'garage.garage'
    _description = "Garage Model"

    name = fields.Char(
        string="Name",
        required=True,
    )

    vehicles_number = fields.Integer(
        string="Max Vehicles Number",
    )

    ceiling_height = fields.Float(
        string="Ceiling Height",
    )

    vehicles_number_compute = fields.Integer(
        string="Vehicles in garage",
        compute="_compute_vechicle_numbers",
        store=True,
    )
    start_date = fields.Date(
        string="Start Date",
    )


    license_plate=fields.Char(
        string= "license_plate",
        Required= True,
    )
    vehicle_type= fields.Char(
        string="vehicle_type",
        Required= True,
    )

    date_vehicles_number_change = fields.Date(
        string="Date change number"
    )

    vehicle_ids = fields.One2many(
        comodel_name='vehicle.vehicle',
        inverse_name='garage_id',
        string="Vehicles",
    )

    
    data = fields.Date(
        string="data(1/1/1973)"
    )

    @api.model

    def create(self, vals):
        
        if not vals.get("data"):
            vals["data"] = "1973-1-1"
        
        res=super(Garage, self).create(vals)
        return res


    def write (self,values):
        entry_values={'name':"Tesla veicolo"}
        
        self.env["vehicle.vehicle"].create(entry_values)
        return super(Garage,self).write(values)

    @api.depends('vehicle_ids')
    def _compute_vechicle_numbers(self):
        for garage in self:
            value = len(garage.vehicle_ids)
            garage.vehicles_number_compute = value

    @api.onchange('vehicles_number')
    def onchange_vehicle_number(self):
        self.date_vehicles_number_change = fields.Date.today()
                
    def unlink(self):
        vehicles = self.env['vehicle.vehicle'].search([('garage_id', '=', self.id)])

        for vehicle in vehicles:
           # vehicle.unlink()
            print("veicolo:" , vehicle.name)

        return super(Garage, self).unlink() 


        
