from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.LamViec import LamViecModel
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from .utils import *

class LamViecView(ModelView):
    datamodel = SQLAInterface(LamViecModel)
    list_columns = ['MANHANVIEN', 'MALICHLAM', 'DIEMDANH', 'VITRI', 'LichLam.MALICHLAM', 'LichLam.NAM', 'LichLam.TUAN', 'LichLam.THU', 'LichLam.THOIGIAN']
    
    list_title = "Làm Việc"    
    label_columns = {
            'LichLam.MALICHLAM' : 'MALICHLAM',
            'LichLam.NAM' : 'NAM',
            'LichLam.TUAN' : 'TUAN',
            'LichLam.THU' : 'THU',
            'LichLam.THOIGIAN' : 'THOIGIAN'
        }
    
    route_base = "/lam_viec"
        
    base_filters = [['nhanvien.TAIKHOAN', FilterEqualFunction, lambda: get_user_id()]]


class QuanLyLamViecView(ModelView):
    datamodel = SQLAInterface(LamViecModel)
    list_columns = ['MANHANVIEN', 'MALICHLAM', 'DIEMDANH', 'VITRI']
    
    list_title = "Quản Lý Làm Việc"
    
    route_base = "/quan_ly_lam_viec"