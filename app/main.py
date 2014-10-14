import os

import webapp2

from app import routes


webapp2_config = {'webapp2_extras.sessions': {
    'webapp2_extras.jinja2': {'template_path': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')}
}}

application = webapp2.WSGIApplication(debug=True, config=webapp2_config)

routes.add_routes(application)