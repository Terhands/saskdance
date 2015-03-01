from google.appengine.ext import ndb


class EventModel(ndb.Model):

    event_time = ndb.StringProperty(indexed=False, required=True)
    location = ndb.StringProperty(indexed=False, required=True)

    band = ndb.StringProperty(indexed=False, required=False)
    name = ndb.StringProperty(indexed=False, required=False)
    description = ndb.StringProperty(indexed=False, required=False)
    cost = ndb.StringProperty(indexed=False, required=False)
    contact_email = ndb.StringProperty(indexed=False, required=False)
    contact_phone = ndb.StringProperty(indexed=False, required=False)
    photo_path = ndb.StringProperty(indexed=False, required=False)

    @classmethod
    def get_events(cls):
        return cls.query().order().fetch()

    @staticmethod
    def build_key(key_id):
        return ndb.Key(EventModel, key_id)