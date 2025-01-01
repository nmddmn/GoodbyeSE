from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.LichLam import LichLamModel
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from .utils import *

class LichLamView(ModelView):
    datamodel = SQLAInterface(LichLamModel)
    
    route_base = "/lich_lam"
    
    # default_view = "test"
    
    base_filters = [['NhanVien.MANHANVIEN', FilterEqualFunction, lambda: None if is_admin() else get_user_id()]]
