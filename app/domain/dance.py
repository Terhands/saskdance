import logging
from app.models.dance import DanceModel


class DanceConstants(object):

    START_TIME = 'event_start'
    END_TIME = 'event_end'
    LOCATION = 'location'
    DESCRIPTION = 'description'
    COST = 'cost'
    EMAIL = 'contact_email'
    PHONE = 'contact_phone'
    PHOTO = 'photo_path'
    BAND = 'band'


def build_dance(start_time, location, **kwargs):
    dance = DanceModel(event_start=start_time,
                       location=location,
                       event_end=kwargs.get(DanceConstants.END_TIME),
                       description=kwargs.get(DanceConstants.DESCRIPTION),
                       cost=kwargs.get(DanceConstants.COST),
                       contact_email=kwargs.get(DanceConstants.EMAIL),
                       contact_phone=kwargs.get(DanceConstants.PHONE),
                       photo_path=kwargs.get(DanceConstants.PHOTO),
                       band=kwargs.get(DanceConstants.BAND))

    dance_id = kwargs.get('id')
    if dance_id:
        dance.key = DanceModel.build_key(dance_id)

    return dance


def save_dance(dance):
    try:
        dance.put()
        return dance
    except Exception, e:
        logging.debug(e.message)