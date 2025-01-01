from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.NhanVien import NhanVienModel
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from .utils import *

class NhanVienView(ModelView):
    datamodel = SQLAInterface(NhanVienModel)
    
    route_base = "/nhan_vien"
    
    # default_view = "test"
    
    base_filters = [['NhanVien.MANHANVIEN', FilterEqualFunction, lambda: None if is_admin() else get_user_id()]]
    
    @expose('/test')
    @has_access
    def test(self):
        # return "Hello World"
    
        param1 = "Hello World"
        self.update_redirect()
        return self.render_template('profile.html', param1 = param1)