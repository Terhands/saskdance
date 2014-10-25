from app.web import build_error_message
from app.web.admin import AdminBaseHandler
from app.domain import dance

from datetime import datetime


class AdminDancesHandler(AdminBaseHandler):

    def get(self):
        """
        Display all dance events
        """
        # TODO get dances in month sections
        # TODO build months programmatically - current first, then ordered
        data = {'months': [{'month': 'january', 'dances': []},
                           {'month': 'february', 'dances': []},
                           {'month': 'march', 'dances': []},
                           {'month': 'april', 'dances': []},
                           {'month': 'may', 'dances': []},
                           {'month': 'june', 'dances': []},
                           {'month': 'july', 'dances': []},
                           {'month': 'august', 'dances': []},
                           {'month': 'september', 'dances': []},
                           {'month': 'october', 'dances': []},
                           {'month': 'november', 'dances': []},
                           {'month': 'december', 'dances': []}],
                'current_month': 0}

        self.render_response('admin/dashboard/dances/dances_overview.html', params=data)


class AddDancesHandler(AdminBaseHandler):

    def get(self):
        self.render_response('admin/dashboard/dances/add_dance.html')

    def put(self):
        """
        Create a new dance event
        """
        dance_dict = {}
        if dance.create_dance(datetime(2014, 1, 1), "123 Fake Street, Saskatoon", **dance_dict):
            self.redirect(self.uri_for('admin-dances'))
        else:
            self.render_response('add_dance.html',
                                 params=build_error_message('Could not create dance. Check logs for details'))

    def post(self):
        """
        Update an existing dance event
        """
        pass