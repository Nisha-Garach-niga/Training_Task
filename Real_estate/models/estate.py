from contextlib import nullcontext
from email.policy import default
from odoo import models, fields, _, api
from odoo.exceptions import UserError


class real_estate(models.Model):

    @api.depends('garden_area', 'living_area')
    def _property_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    def _inverse_area(self):
        self.garden_area = self.living_area = self.total_area/2

    def _search_area(self, operator, value):
        self.env.cr.execute(
            "SELECT id from real_estate where total_area %s %s" % (operator, value))
        ids = self.env.cr.fetchall()
        return [('id', 'in', [id[0] for id in ids])]

    def _get_description(self):
        if self.env.context.get('is_my_property'):
            return self.env.user.name + '\'s Property'

    _inherit = [
        'image.mixin',
    ]

    _name = "real.estate"
    _description = "Real Estate"
    name = fields.Char(name="Title")
    image = fields.Image()
    postcode = fields.Char()
    description = fields.Text(default=_get_description)
    selling_price = fields.Float()
    bedroom = fields.Integer(default=2)
    date_availablity = fields.Date()
    excepted_price = fields.Float(default=0)
    best_offer = fields.Float(compute='_property_best_offer')
    living_area = fields.Integer()
    total_area = fields.Integer(
        compute=_property_total_area, inverse=_inverse_area, search=_search_area)
    garden_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
    validity = fields.Integer()
    deadline = fields.Date()
    proprty_tags = fields.Many2many('property.tags')
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_type_id = fields.Many2one('estate.property.type')
    property_offer_ids = fields.One2many('estate.offer', 'property_id')
    property_offer_ids_count = fields.Integer(compute="action_offer_ids_show")
    # partner_name = fields.Many2one(
    #     'res.users', string='Company', default=lambda self: self.env.user, readonly=True)
    partner_name = fields.Many2one('res.partner', string='Company',
                                   default=lambda self: self.env.user.partner_id.id, readonly=True)
    state = fields.Selection(string='Status', required=True, readonly=True, copy=False, tracking=True, selection=[
        ('open', 'New'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ], default='open')
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    seller_id = fields.Many2one("res.users", string="Salesman")
    active = fields.Boolean()

    @api.model
    def create(self,val):
        print("Before Values ::: ",val)
        # print("Self ::: ",self)
        val['active'] = True
        print("After Values ::: ",val)
        rtn = super(real_estate,self).create(val)
        print("Return ::: ",rtn)
        return rtn

    @api.onchange('garden')
    def _onchange_property_id(self):
        if self.garden == True:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = None
            self.garden_orientation = ''

    @api.constrains('excepted_price')
    def _check_excepted_price(self):
        if self.excepted_price <= 0:
            raise UserError(_("Excepted Price should be Positive."))

    @api.depends('property_offer_ids.price')
    def _property_best_offer(self):
        # min_price = max(self.property_offer_ids.mapped('price'))
        # if self.excepted_price >= min_price:
        #     self.best_offer = min_price
        # else:
        #     self.best_offer = 0
        max_price = 0
        for record in self.property_offer_ids:
            if record.price >= max_price:
                max_price = record.price
        self.best_offer = max_price

    def button_sold(self):
        ''' Move the state from 'new' to 'sold'. '''
        return self.write({'state': 'sold'})

    def button_reopen(self):
        ''' Move the state back to the 'open' state. '''
        return self.write({'state': 'open'})

    def button_cancelled(self):
        """Move the state to the 'cancelled' state."""
        return self.write({'state': 'cancelled'})

    def action_offer_ids_show(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "Real_estate.Offers_action")
        action['domain'] = [('id', 'in', self.property_offer_ids.ids)]

        for lead in self:
            lead.property_offer_ids_count = len(lead.property_offer_ids)

        return action


class real_estate_property_type(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char()
    property_ids = fields.One2many('real.estate', 'property_type_id')


###############  For Debugging ###############
    # from pudb import set_trace; set_trace()
    # import pudb
    # pudb.self_trace()
##############################################

    # def action_confirm(self):
    #     for session in self:
    #         for attendee in session.attendee_ids:
    #             print ("Attendee ::: ", attendee.name)
