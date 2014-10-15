import webapp2
import json
from webapp2_extras import jinja2
from webapp2_extras import auth, sessions


class BaseHandler(webapp2.RequestHandler):
    """
    base request handler for browser-based requests
    """
    def dispatch(self):
        try:
            # Dispatch the request.
            super(BaseHandler, self).dispatch()
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

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

    def render_response(self, _template, params=None):
        # Renders a template and writes the result to the response.
        if not params:
            params = {}

        rv = self.jinja2.render_template(_template, **params)

        self.response.write(rv)


class BaseApiHandler(webapp2.RequestHandler):
    """
    base request Handler for API traffic
    """
    def render_response(self, result):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(result))