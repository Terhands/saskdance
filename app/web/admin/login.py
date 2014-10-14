from app.web import BaseHandler


class LoginHandler(BaseHandler):

    def get(self):
        self.render_response('admin/login.html')

    def post(self):
        if self.request.get('password') == 'test':
            # need to actually get the user (need to have some kind of user bootstrap to set the UserModel
            self.redirect(self.uri_for('admin-dashboard'))
        else:
            self.render_response('admin/login.html', params={'error': 'Wrong Password!'})
