import openerp.http as http
import odoo,werkzeug
from contextlib import closing
from odoo.tools.translate import _
from odoo.addons.web.controllers import main
from odoo.http import request

class Academy(http.Controller):

    @http.route('/web/login/saas/',type='http',auth='none')
    def web_login_saass(self,**kw):
        request.params['login_success'] = False
      	old_uid = request.uid
	uid = request.session.authenticate(kw['database'], kw['username'], kw['pass'])
     	if uid is not False:
                request.params['login_success'] = True
                redirect = '/web'
                return http.redirect_with_hash(redirect)
        request.uid = old_uid
        values['error'] = _("Wrong login/password")
        return request.render('web.login', values)
