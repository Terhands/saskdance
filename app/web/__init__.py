import webapp2
import json
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):
    """
    base request handler for browser-based requests
    """
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

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