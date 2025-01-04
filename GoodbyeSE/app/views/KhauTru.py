from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.KhauTru import KhauTruModel
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from .utils import *

class KhauTruView(ModelView):
    datamodel = SQLAInterface(KhauTruModel)
    list_columns = ["MAKHAUTRU", "TENKHAUTRU", "SOTIEN"]
    
    list_title = "Khấu Trừ"
    
    route_base = "/khau_tru"
    
    # default_view = "test"
