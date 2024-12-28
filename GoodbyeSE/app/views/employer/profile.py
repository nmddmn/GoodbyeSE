from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access

# class EmployerProfileView(ModelView):
class EmployerProfileView(BaseView):
    # datamodel = SQLAInterface(MyModel)
    
    route_base = "/profile"
    
    @expose('/list')
    @has_access
    def list(self):
        return "Hello World"