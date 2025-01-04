from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.PhuCap import PhuCapModel
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from .utils import *

class PhuCapView(ModelView):
    datamodel = SQLAInterface(PhuCapModel)
    list_columns = ["MAPHUCAP", "TENPHUCAP", "SOTIEN"]
    
    list_title = "Phụ Cấp"
    
    route_base = "/phu_cap"