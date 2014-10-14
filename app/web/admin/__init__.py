import webapp2

from app.web import BaseHandler

from webapp2_extras import auth, sessions


class AdminBaseHandler(BaseHandler):

    def dispatch(self):
        """
        Get a session store for this request.
        """
        self.session_store = sessions.get_store(request=self.request)
        if not not self.user:
            self.redirect_to('login', _abort=True)
        try:
            super(AdminBaseHandler, self).dispatch()
        finally:
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def auth(self):
        return auth.get_auth()

    @webapp2.cached_property
    def session_store(self):
        return sessions.get_store(request=self.request)

    @webapp2.cached_property
    def user_model(self):
        return self.auth.store.user_model

    @property
    def user(self):
        current_user = self.auth.get_user_by_session()
        return self.user_model.get_by_id(current_user['user_id']) if current_user else None