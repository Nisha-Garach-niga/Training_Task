from odoo import models, fields, _, api

class property_tags(models.Model):
    _name = "property.tags"
    _description = "Property Tags"

    name = fields.Char()
    color = fields.Integer()

class Estate_offer(models.Model):
    _name = 'estate.offer'
    _description = 'Estate Offer'

    price = fields.Float()
    status = fields.Selection([('accepted' , 'Accepted'),('rejected','Rejected')])
    partner_id = fields.Many2one('res.partner')
    property_id = fields.Many2one('real.estate')
    property_type_id = fields.Many2one('estate.property.type')


    def action_accepted(self):
        for record in self:
            record.status = "accepted"

    def action_rejected(self):
        for record in self:
            record.status = "rejected"

class Buyer_partner(models.Model):
    _inherit = 'res.partner'

    is_buyer = fields.Boolean()