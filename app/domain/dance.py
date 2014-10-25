import logging
from app.models.dance import DanceModel


class DanceConstants(object):

    START_TIME = 'event_start'
    END_TIME = 'event_end'
    LOCATION = 'location'
    TITLE = 'title'
    DESCRIPTION = 'description'
    COST = 'cost'
    EMAIL = 'contact_email'
    PHONE = 'contact_phone'
    PHOTO = 'photo_path'


def create_dance(start_time, location, **kwargs):

    try:
        dance = DanceModel(event_start=start_time,
                           location=location,
                           event_end=kwargs.get(DanceConstants.END_TIME),
                           title=kwargs.get(DanceConstants.TITLE),
                           description=kwargs.get(DanceConstants.DESCRIPTION),
                           cost=kwargs.get(DanceConstants.COST),
                           contact_email=kwargs.get(DanceConstants.EMAIL),
                           contact_phone=kwargs.get(DanceConstants.PHONE),
                           photo_path=kwargs.get(DanceConstants.PHOTO))
        dance.put()
        return dance
    except Exception, e:
        logging.debug(e.message)