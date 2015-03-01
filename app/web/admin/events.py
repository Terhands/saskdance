from app.web import build_error_message
from app.web.admin import AdminBaseHandler
from app.domain import event
from app.domain.event import EventConstants
from app.models.event import EventModel


class AdminEventsHandler(AdminBaseHandler):

    def get(self):
        """
        Display all events
        """
        events = EventModel.get_events()
        self.render_response('admin/dashboard/events/events_overview.html', params={'events': events})


class AddEventsHandler(AdminBaseHandler):

    def get(self):
        self.render_response('admin/dashboard/events/add_event.html')

    def post(self):
        """
        Create a new dance event
        """
        event_dict = create_event_dict(self.request)
        dance_model = event.build_event(**event_dict)

        if event.save_event(dance_model):
            self.redirect(self.uri_for('admin-events'))
        else:
            self.render_response('add_event.html',
                                 params=build_error_message('Could not create event. Check logs for details'))


class EditEventsHandler(AdminBaseHandler):

    def get(self):
        event_id = int(self.request.get('id'))
        event_model = EventModel.build_key(event_id).get()
        event_dict = event_model.to_dict()
        event_dict['id'] = event_id
        event_dict['event_date'] = event_model.event_datetime.strftime('%m/%d/%Y')
        event_dict['event_time'] = event_model.event_datetime.strftime('%H:%M %p')
        self.render_response('admin/dashboard/events/edit_event.html', params=event_dict)

    def post(self):
        """
        Update an existing dance event
        """
        event_id = int(self.request.get('id'))
        event_dict = create_event_dict(self.request)
        event_dict['id'] = event_id
        event_model = event.build_event(**event_dict)

        if event.save_event(event_model):
            self.redirect(self.uri_for('admin-events'))
        else:
            self.render_response('edit_event.html',
                                 params=build_error_message('Could not create dance. Check logs for details'))


def create_event_dict(request):

    event_time = request.get('event_date') + ' ' + request.get('event_time')
    name = request.get('name')
    description = request.get('description')
    cost = request.get('cost')
    email = request.get('email')
    phone = request.get('phone')
    photo = request.get('event_photo')
    location = request.get('location')
    band = request.get('band')

    dance_dict = {
        EventConstants.EVENT_TIME: event_time,
        EventConstants.NAME: name,
        EventConstants.DESCRIPTION: description,
        EventConstants.COST: cost,
        EventConstants.EMAIL: email,
        EventConstants.PHONE: phone,
        EventConstants.PHOTO: photo,
        EventConstants.BAND: band,
        EventConstants.LOCATION: location
    }

    return dance_dict