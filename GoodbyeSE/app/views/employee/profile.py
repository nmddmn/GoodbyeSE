from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.profile import EmployeeProfileModel
from .employee import EmployeeView
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from ..utils import *

class EmployeeProfileView(ModelView):
# class EmployeeProfileView(BaseView):
    datamodel = SQLAInterface(EmployeeProfileModel)
    
    route_base = EmployeeView.route_base + "/profile"
    
    default_view = "test"
    
    base_filters = [['id', FilterEqualFunction, lambda: None if is_admin() else get_user_id()]]
    
    @expose('/test')
    @has_access
    def test(self):
        # return "Hello World"
    
        param1 = "Hello World"
        self.update_redirect()
        return self.render_template('profile.html', param1 = param1)