from odoo import http
from odoo.http import request

class RealEstate(http.Controller):

    @http.route('/first_r', auth="public")
    def hello(self, **kw):
        return "Hello World From Hello"

    @http.route('/second_r', auth="user")
    def hello_user(self, **kw):
        return "Hello World From Hello %s" % (request.env.user.name)

    @http.route('/hello_template')
    def hello_temp(self, **kw):
        return request.render('Real_estate.hello_world')

    @http.route('/estate_property', auth="public", website=True)
    def hello_template_user(self, **kw):
        # properties = request.env['real.estate'].search([('state', '=', 'sold')])
        properties = request.env['real.estate'].search([])
        print("properties ::: ", properties)
        return request.render('Real_estate.estate_property', {'user': request.env.user, 'properties': properties})

    @http.route('/property', auth="public", website=True)
    def property_template_user(self, **kw):
        return request.render('Real_estate.property_template', {
            'user': request.env.user, 
            'properties': request.env['real.estate'].sudo().search([], limit=8)
        })

    @http.route('/property/<model("real.estate"):property>', auth="public", website=True)
    def property_details(self,property=False, **kw):
        if property:
            # print("properties ::: ", property)
            return request.render('Real_estate.property_detail', {
                'property': property
            })
