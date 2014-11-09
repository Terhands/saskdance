import webapp2

from app.web import BaseHandler

from webapp2_extras import sessions


class AdminBaseHandler(BaseHandler):

    def dispatch(self):
        """
        Get a session store for this request.
        """
        self.session_store = sessions.get_store(request=self.request)
        if not self.user:
            self.redirect_to('login', _abort=True)
        try:
            super(AdminBaseHandler, self).dispatch()
        finally:
            self.session_store.save_sessions(self.response)

    def render_response(self, _template, params={}):
        params.update({'role': 'admin'})
        super(AdminBaseHandler, self).render_response(_template, params=params)