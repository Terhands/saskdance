from app.web import BaseHandler
from app.models.event import EventModel


class EventsHandler(BaseHandler):

    def get(self):
        """
        Display all events
        """
        events = EventModel.get_events()
        data = {'events': events}
        self.render_response('user/events.html', params=data)