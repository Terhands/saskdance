from app.web import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        self.render_response('index.html')