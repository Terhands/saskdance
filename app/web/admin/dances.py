import json
import time

from app.web import build_error_message
from app.web.admin import AdminBaseHandler
from app.domain import dance
from app.domain.dance import DanceConstants
from app.models.dance import DanceModel

from datetime import datetime


class AdminDancesHandler(AdminBaseHandler):

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
                    'band': d.band,
                    'location': d.location,
                    'date': datetime.strftime(d.event_start, "%b %d, %Y %I:%M%p"),
                    'price': d.cost
                })

        # TODO get dances in month sections
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
                'current_month': 11}

        self.render_response('admin/dashboard/dances/dances_overview.html', params=data)


class AddDancesHandler(AdminBaseHandler):

    def get(self):
        self.render_response('admin/dashboard/dances/add_dance.html')

    def post(self):
        """
        Create a new dance event
        """
        title = self.request.get('title')
        description = self.request.get('description')

        start_date = None
        if self.request.get('start_date') and self.request.get('start_time'):
            start_date = datetime.strptime(self.request.get('start_date') + ":" + self.request.get('start_time'),
                                           "%Y/%m/%d:%H:%M")
        elif self.request.get('start_date'):
            start_date = datetime.strptime(self.request.get('start_date'), "%Y/%m/%d")

        end_date = None
        if start_date and self.request.get('end_time'):
            end_date = datetime.strptime(self.request.get('start_date') + ":" + self.request.get('end_time'),
                                         "%Y/%m/%d:%H:%M")

        cost = self.request.get('cost')
        email = self.request.get('email')
        phone = self.request.get('phone')
        photo = self.request.get('event_photo')
        location = self.request.get('location')
        band = self.request.get('band')

        dance_dict = {
            DanceConstants.END_TIME: end_date,
            DanceConstants.TITLE: title,
            DanceConstants.DESCRIPTION: description,
            DanceConstants.COST: cost,
            DanceConstants.EMAIL: email,
            DanceConstants.PHONE: phone,
            DanceConstants.PHOTO: photo,
            DanceConstants.BAND: band
        }

        if dance.create_dance(start_date, location, **dance_dict):
            self.redirect(self.uri_for('admin-dances'))
        else:
            self.render_response('add_dance.html',
                                 params=build_error_message('Could not create dance. Check logs for details'))

    # def post(self):
    #     """
    #     Update an existing dance event
    #     """
    #     pass