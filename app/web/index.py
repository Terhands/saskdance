from app.web import BaseHandler


class IndexHandler(BaseHandler):

    def get(self):
        self.redirect(self.uri_for('dances'))