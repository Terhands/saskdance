from app.web.admin import AdminBaseHandler


class DashboardHandler(AdminBaseHandler):

    def get(self):
        if self.user:
            self.render_response('admin/dashboard/dashboard.html')
        else:
            self.redirect(self.uri_for('login'))