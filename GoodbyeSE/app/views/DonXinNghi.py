from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.DonXinNghi import DonXinNghiModel
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from .utils import *

class DonXinNghiView(ModelView):
    datamodel = SQLAInterface(DonXinNghiModel)
    list_columns = ['MADONXINNGHI', 'LYDO', 'TRANGTHAI', 'THOIGIANGUI', 'MALAMVIEC', 'MANHANVIEN']
    # edit_columns = ['LYDO', 'THOIGIANGUI', 'MALAMVIEC', 'MANHANVIEN']
    # add_columns = ['LYDO', 'THOIGIANGUI', 'MALAMVIEC', 'MANHANVIEN']
    
    list_title = "Đơn Xin Nghỉ"
    
    route_base = "/don_xin_nghi"
        
    base_filters = [['NhanVien.TAIKHOAN', FilterEqualFunction, lambda: get_user_id()]]


class QuanLyDonXinNghiView(ModelView):
    datamodel = SQLAInterface(DonXinNghiModel)
    list_columns = ['MADONXINNGHI', 'LYDO', 'TRANGTHAI', 'THOIGIANGUI', 'MALAMVIEC']
    
    list_title = "Quản Lý Đơn Xin Nghỉ"
    
    route_base = "/quan_ly_don_xin_nghi"
