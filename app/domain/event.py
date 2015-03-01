import logging
import datetime
from app.models.event import EventModel


class EventConstants(object):

    EVENT_ID = 'id'
    EVENT_TIME = 'event_time'
    NAME = 'name'
    LOCATION = 'location'
    DESCRIPTION = 'description'
    COST = 'cost'
    EMAIL = 'contact_email'
    PHONE = 'contact_phone'
    PHOTO = 'photo_path'
    BAND = 'band'


def build_event(**kwargs):

    event_datetime = datetime.datetime.strptime(kwargs.get(EventConstants.EVENT_TIME), "%m/%d/%Y %H:%M %p")

    event = EventModel(event_datetime=event_datetime,
                       location=kwargs.get(EventConstants.LOCATION),
                       name=kwargs.get(EventConstants.NAME),
                       description=kwargs.get(EventConstants.DESCRIPTION),
                       cost=kwargs.get(EventConstants.COST),
                       contact_email=kwargs.get(EventConstants.EMAIL),
                       contact_phone=kwargs.get(EventConstants.PHONE),
                       photo_path=kwargs.get(EventConstants.PHOTO),
                       band=kwargs.get(EventConstants.BAND))

    dance_id = kwargs.get(EventConstants.EVENT_ID)
    if dance_id:
        event.key = EventModel.build_key(dance_id)

    return event


def save_event(event):
    try:
        event.put()
        return event
    except Exception, e:
        logging.debug(e.message)
