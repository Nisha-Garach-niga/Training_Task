from odoo import models, fields, _, api
from datetime import date
from dateutil.relativedelta import relativedelta

class Lease_Property(models.Model):
    _inherit = 'real.estate'

    lease_name = fields.Char()

class Lease_Property_(models.Model):
    _name = 'lease.property.tag'
    _inherit = 'property.tags'

    lease_tag = fields.Many2one('property.tags')

class Lease_Property_name(models.Model):
    _name = 'lease.property'
    _inherits = {'estate.property.type' : 'property_id'}

    property_id = fields.Many2one('estate.property.type')
    lease_duration = fields.Float()
    lease_rent_monthly = fields.Float()
    # start_date = fields.Datetime()
    start_date = fields.Datetime(default=fields.Datetime.now, required=True)
    end_date = fields.Datetime()
    # end_date = start_date + relativedelta(days=5)
    # if start_date != None:
    #     end_date = start_date + relativedelta(days=5)

    # def _set_end_time(self):
    #     for record in self:
    #         record.end_date = record.start_date + relativedelta(30)

    @api.onchange('start_date')
    def _onchange_start_date(self):
        for record in self:
            record.end_date = record.start_date + relativedelta(days=30)


