from app.web import BaseHandler


class DancesHandler(BaseHandler):

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

        self.render_response('user/dances.html', params=data)