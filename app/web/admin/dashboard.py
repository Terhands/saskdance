from app.web.admin import AdminBaseHandler


class DashboardHandler(AdminBaseHandler):

    def get(self):
        self.render_response('admin/dashboard/dashboard.html', params={'role': 'admin'})