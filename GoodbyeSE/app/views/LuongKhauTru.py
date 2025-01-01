from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.LuongKhauTru import LuongKhauTruModel
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from .utils import *

class LuongKhauTruView(ModelView):
    datamodel = SQLAInterface(LuongKhauTruModel)
    list_columns = ['MAKHAUTRU', 'MAPHUCAP']
    
    route_base = "/luong_khau_tru"
    
    # default_view = "test"
    
    base_filters = [['NhanVien.MANHANVIEN', FilterEqualFunction, lambda: None if is_admin() else get_user_id()]]
