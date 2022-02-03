# from odoo import models, fields, _, api

# class property_tags(models.Model):
#     _name = "property.tags"
#     _description = "Property Tags"

#     name = fields.Char()
#     color = fields.Integer()

# class Estate_offer(models.Model):
#     _name = 'estate.offer'
#     _description = 'Estate Offer'

#     price = fields.Float()
#     status = fields.Selection([('accepted' , 'Accepted'),('rejected','Rejected')])
#     partner_id = fields.Many2one('res.partner')
#     property_id = fields.Many2one('real.estate')
#     # property_type_Id = fields.Many2one(related='estate.property.type', store=True)
#     property_type_id = fields.Many2one('estate.property.type')


#     def action_accepted(self):
#         for record in self:
#             record.status = "accepted"
#             #set the buyer and selling prize
#             # record.partner_id.selling_price = record.selling_price
#             # record.property_id.buyer_id= record.partner_id

#     def action_rejected(self):
#         for record in self:
#             record.status = "rejected"