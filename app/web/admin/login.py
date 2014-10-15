from app.web import BaseHandler
from webapp2_extras.appengine.auth.models import User


class LoginHandler(BaseHandler):

    def get(self):
        if len(User.query().fetch()) == 0:
            bootstrap('test')

        self.render_response('admin/login.html')

    def post(self):
        password = self.request.get('password')
        try:
            self.auth.get_user_by_password('giddingsl', password)
            self.redirect(self.uri_for('admin-dashboard'))
        except Exception:
            self.render_response('admin/login.html', params={'error': 'Wrong Password!'})


def bootstrap(password):
    User.create_user('giddingsl', password_raw=password)