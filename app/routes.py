from webapp2 import Route
from app.web import index
from app.web.admin import login, dashboard, dances
from app.web.users import dances as user_dances

__all__ = ['get_routes',
           'add_routes']

_routes = [

    Route('/admin', handler=login.LoginHandler, name='login'),
    Route('/dashboard', handler=dashboard.DashboardHandler, name='admin-dashboard'),
    Route('/dashboard/dances', handler=dances.AdminDancesHandler, name='admin-dances'),
    Route('/dashboard/dances/add', handler=dances.AddDancesHandler, name='admin-add-dance'),

    Route('/dances', handler=user_dances.DancesHandler, name='dances'),
    Route('/', handler=index.IndexHandler)

]


def get_routes():
    return _routes


def add_routes(app):
    for r in _routes:
        app.router.add(r)
