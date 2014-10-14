from webapp2 import Route
from app.web import index

__all__ = ['get_routes',
           'add_routes']

_routes = [
    Route('/', handler=index.IndexHandler),
]


def get_routes():
    return _routes


def add_routes(app):
    for r in _routes:
        app.router.add(r)
