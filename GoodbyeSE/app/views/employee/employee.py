from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access

class EmployeeView(BaseView):
        
    route_base = "/employee"
    
    default_view = "test"
    
    @expose('/test')
    @has_access
    def test(self):
        # return "Hello World"
    
        param1 = "Hello World"
        self.update_redirect()
        return self.render_template('profile.html', param1 = param1)