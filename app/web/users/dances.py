from datetime import datetime

from app.web import BaseHandler
from app.models.dance import DanceModel


class DancesHandler(BaseHandler):

    def get(self):
        """
        Display all dance events
        """

        dances = DanceModel.get_dances_ordered_by_start_time()

        month_dances = [[], [], [], [], [], [], [], [], [], [], [], []]

        for d in dances:
            now = datetime.utcnow()
            if (d.start_year == now.year and d.start_month >= now.month) or (d.start_year == now.year - 1 and d.start_month < now.month):
                month_dances[d.start_month - 1].append({
                    'title': d.title,
                    'description': d.description,
                    'band': d.band,
                    'location': d.location,
                    'date': datetime.strftime(d.event_start, "%b %d, %Y %I:%M%p"),
                    'price': d.cost
                })

        current_month = int(self.request.get('month')) if self.request.get('month') else 0

        # TODO build months programmatically - current first, then ordered
        data = {'months': [{'month': 'january', 'dances': month_dances[0]},
                           {'month': 'february', 'dances': month_dances[1]},
                           {'month': 'march', 'dances': month_dances[2]},
                           {'month': 'april', 'dances': month_dances[3]},
                           {'month': 'may', 'dances': month_dances[4]},
                           {'month': 'june', 'dances': month_dances[5]},
                           {'month': 'july', 'dances': month_dances[6]},
                           {'month': 'august', 'dances': month_dances[7]},
                           {'month': 'september', 'dances': month_dances[8]},
                           {'month': 'october', 'dances': month_dances[9]},
                           {'month': 'november', 'dances': month_dances[10]},
                           {'month': 'december', 'dances': month_dances[11]}],
                'current_month': current_month}

        self.render_response('user/dances.html', params=data)