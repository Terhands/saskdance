from google.appengine.ext import ndb


class DanceModel(ndb.Model):

    event_start = ndb.DateTimeProperty(indexed=True, required=True)
    start_year = ndb.ComputedProperty(lambda dance: dance.event_start.year, indexed=True)
    start_month = ndb.ComputedProperty(lambda dance: dance.event_start.month, indexed=True)

    event_end = ndb.DateTimeProperty(indexed=False, required=False)
    location = ndb.StringProperty(indexed=False, required=True)

    title = ndb.StringProperty(indexed=False, required=False)
    band = ndb.StringProperty(indexed=False, required=False)
    description = ndb.StringProperty(indexed=False, required=False)
    cost = ndb.StringProperty(indexed=False, required=False)
    contact_email = ndb.StringProperty(indexed=False, required=False)
    contact_phone = ndb.StringProperty(indexed=False, required=False)
    photo_path = ndb.StringProperty(indexed=False, required=False)

    @classmethod
    def get_dances_ordered_by_start_time(cls):
        return cls.query().order(cls.event_start).fetch()

    @classmethod
    def get_dances_in(cls, year, month):
        return cls.query().filter(cls.start_year == year)\
                          .filter(cls.start_month == month)\
                          .order(cls.event_start)\
                          .fetch()



