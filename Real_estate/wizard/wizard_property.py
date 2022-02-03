from odoo import _, models, api, fields

class WizardProperty(models.TransientModel):
    _name = 'estate.property.wizard'

    # name = fields.Char()
    buyer_id = fields.Many2one("res.partner", string="Buyer")

    price = fields.Float()
    status = fields.Selection([('accepted' , 'Accepted'),('rejected','Rejected')])
    partner_id = fields.Many2one('res.partner')

    def action_assign_buyer(self):
        # print('--------------------Success--------------------')
        self.ensure_one()
        activeIds = self.env.context.get('active_ids')
        self.env['real.estate'].browse(activeIds).write({'buyer_id': self.buyer_id.id})
        return True

    def action_make_offer(self):
        # print('--------------------Success--------------------',self.property_offer_ids.id)
        self.ensure_one()
        activeIds = self.env.context.get('active_ids')
        Offer = self.env['estate.offer']
        data = {
            'price' : self.price,
            'status' : self.status,
            'partner_id' : self.partner_id.id
        }
        for property in self.env['real.estate'].browse(activeIds):
            ## Method 1
            # data['property_id'] = property.id
            # Offer.create(data)

            # Method 2
            property.write({'property_offer_ids' : [(0,0,data)]})
            ##                                       t,i
            ## here t -> create,write,link,delete,...etc
            ## here i -> id (jis id me perform karna ho)

        return True
