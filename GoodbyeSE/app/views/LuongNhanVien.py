from flask import render_template, redirect, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.LuongNhanVien import LuongNhanVienModel
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from .utils import *
from flask_appbuilder.exceptions import FABException
import io
from flask import send_file
from openpyxl import Workbook
from app import db

import sqlite3

class LuongNhanVienView(ModelView):
    datamodel = SQLAInterface(LuongNhanVienModel)
    list_columns = ['MATHONGTINLUONG', 'MALOAILUONG', 'NhanVien.HOTEN', 'THANG', 'NAM', 'SONGAYLAM', 'SONGAYVANG',
                    'LUONGNHAN', 'Luong.TENLOAILUONG', 'Luong.VITRI', 'Luong.HESOLUONG', 'Luong.LUONGCOBAN']
    
    list_title = "Lương Nhân Viên"
    label_columns = {
            'NhanVien.HOTEN' : 'Họ Tên',
        }
    
    route_base = "/luong_nhan_vien"
        
    base_filters = [['NhanVien.TAIKHOAN', FilterEqualFunction, lambda: get_user_id()]]
    
    @expose("/calculate/")
    def calculate(self):
        print("calculate")
        
        conn = sqlite3.connect('C:/Users/Admin/Desktop/GoodbyeSE/GoodbyeSE/app.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE LuongNhanVien 
            SET LUONGNHAN = (
                SELECT ROUND(
                    (Luong.LUONGCOBAN * 
                    Luong.HESOLUONG * 
                    outer_lnv.SONGAYLAM/(outer_lnv.SONGAYLAM + outer_lnv.SONGAYVANG)) +
                    COALESCE(SUM(PhuCap.SOTIEN), 0) + 
                    COALESCE(SUM(KhauTru.SOTIEN), 0)
                )
                FROM LuongNhanVien AS outer_lnv
                JOIN Luong ON outer_lnv.MALOAILUONG = Luong.MALOAILUONG
                LEFT JOIN LuongNhanVien_PhuCap ON LuongNhanVien_PhuCap.LuongNhanVien_MATHONGTINLUONG = outer_lnv.MATHONGTINLUONG 
                LEFT JOIN PhuCap ON PhuCap.MAPHUCAP = LuongNhanVien_PhuCap.PhuCap_MAPHUCAP
                LEFT JOIN LuongNhanVien_KhauTru ON LuongNhanVien_KhauTru.LuongNhanVien_MATHONGTINLUONG = outer_lnv.MATHONGTINLUONG
                LEFT JOIN KhauTru ON KhauTru.MAKHAUTRU = LuongNhanVien_KhauTru.KhauTru_MAKHAUTRU
                WHERE outer_lnv.MATHONGTINLUONG = LuongNhanVien.MATHONGTINLUONG
                GROUP BY outer_lnv.MATHONGTINLUONG, Luong.LUONGCOBAN, Luong.HESOLUONG, outer_lnv.SONGAYLAM, outer_lnv.SONGAYVANG
            );
            ''')
        
        conn.commit()
        conn.close()
        
        return redirect("../list")
    
    
    @expose("/list/")
    @has_access
    def list(self):
        self.update_redirect()
        try:
            widgets = self._list()
        except FABException as exc:
            flash(f"An error occurred: {exc}", "warning")
            return redirect(self.get_redirect())
        return self.render_template(
            "custom_list_luong.html", title=self.list_title, widgets=widgets
        )


class QuanLyLuongNhanVienView(LuongNhanVienView):
    datamodel = SQLAInterface(LuongNhanVienModel)
    
    list_title = "Quản lý Lương Nhân Viên"

    route_base = "/quan_ly_luong_nhan_vien"
    
    base_filters = []
    
    @expose("/export_excel/")
    @has_access
    def export_excel(self):
        # Query the data
        records = db.session.query(LuongNhanVienModel).all()

        # Create an Excel file
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Your Model Data"

        # Add header
        sheet.append(['MATHONGTINLUONG', 'MALOAILUONG', 'MANHANVIEN', 'THANG', 'NAM', 'SONGAYLAM', 'SONGAYVANG', 'LUONGNHAN'])

        # Add rows
        for record in records:
            sheet.append([record.MATHONGTINLUONG, record.MALOAILUONG, record.MANHANVIEN, record.THANG, record.NAM, record.SONGAYLAM, record.SONGAYVANG, record.LUONGNHAN])

        # Save to a BytesIO buffer
        output = io.BytesIO()
        workbook.save(output)
        output.seek(0)

        # Send the file
        return send_file(
            output,
            as_attachment=True,
            download_name="your_model.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
