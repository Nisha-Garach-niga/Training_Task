from odoo import http
from odoo.http import request


#  Create controller and render static template and create another controller and render dynamic template with different directives
# You should use directives like t-foreach, t-call- t-field, t-set, t-if, t-else, t-elif, t-att, attf, t-out

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
        # user = request.env.user
        print("properties ::: ", properties)
        # print ("user ::: ", user.partner_id)
        return request.render('Real_estate.estate_property', {'user': request.env.user, 'properties': properties})
