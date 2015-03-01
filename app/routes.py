from webapp2 import Route
from app.web import index
from app.web.admin import login, dashboard, dances, events
from app.web.users import dances as user_dances, events as user_events

__all__ = ['get_routes',
           'add_routes']

_routes = [

    Route('/admin', handler=login.LoginHandler, name='login'),
    Route('/dashboard', handler=dashboard.DashboardHandler, name='admin-dashboard'),
    Route('/dashboard/dances', handler=dances.AdminDancesHandler, name='admin-dances'),
    Route('/dashboard/dances/add', handler=dances.AddDancesHandler, name='admin-add-dance'),
    Route('/dashboard/dances/edit', handler=dances.EditDancesHandler, name='admin-edit-dance'),
    Route('/dashboard/events', handler=events.AdminEventsHandler, name='admin-events'),
    Route('/dashboard/events/add', handler=events.AddEventsHandler, name='admin-add-event'),
    Route('/dashboard/events/edit', handler=events.EditEventsHandler, name='admin-edit-event'),

    Route('/dances', handler=user_dances.DancesHandler, name='dances'),
    Route('/events', handler=user_events.EventsHandler, name='events'),
    Route('/', handler=index.IndexHandler)

]


def get_routes():
    return _routes


def add_routes(app):
    for r in _routes:
        app.router.add(r)
