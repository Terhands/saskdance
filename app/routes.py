from webapp2 import Route
from app.web import index
from app.web.admin import login
from app.web.admin import dashboard

__all__ = ['get_routes',
           'add_routes']

_routes = [

    Route('/admin', handler=login.LoginHandler, name='login'),
    Route('/admin/dashboard', handler=dashboard.DashboardHandler, name='admin-dashboard'),

    Route('/', handler=index.IndexHandler)
]


def get_routes():
    return _routes


def add_routes(app):
    for r in _routes:
        app.router.add(r)
