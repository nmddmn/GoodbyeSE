import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

from app.views.custom_index import CustomIndexView

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview = CustomIndexView)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from app.views.NhanVien import NhanVienView, QuanLyNhanVienView
appbuilder.add_view(NhanVienView, "Thông Tin Nhân Viên", category='Thông Tin Nhân Viên')

appbuilder.add_separator("Thông Tin Nhân Viên")
appbuilder.add_view(QuanLyNhanVienView, "Quản lý Thông Tin Nhân Viên", category='Thông Tin Nhân Viên')

from app.views.LuongNhanVien import LuongNhanVienView, QuanLyLuongNhanVienView
from app.views.Luong import LuongView
from app.views.PhuCap import PhuCapView
from app.views.KhauTru import KhauTruView

appbuilder.add_view(LuongNhanVienView, "Lương Nhân Viên", category='Lương')
appbuilder.add_view(LuongView, "Lương", category='Lương')
appbuilder.add_view(PhuCapView, "Phụ Cấp", category='Lương')
appbuilder.add_view(KhauTruView, "Khấu Trừ", category='Lương')

appbuilder.add_separator("Lương")
appbuilder.add_view(QuanLyLuongNhanVienView, "Quản Lý Lương Nhân Viên", category='Lương')

from app.views.LamViec import LamViecView, QuanLyLamViecView
from app.views.LichLam import LichLamView
from app.views.DonXinNghi import DonXinNghiView, QuanLyDonXinNghiView

appbuilder.add_view(LamViecView, "Làm Việc", category='Công việc')
appbuilder.add_view(LichLamView, "Lịch Làm", category='Công việc')
appbuilder.add_view(DonXinNghiView, "Đơn Xin Nghỉ", category='Công việc')

appbuilder.add_separator("Công việc")
appbuilder.add_view(QuanLyLamViecView, "Quản Lý Làm Việc", category='Công việc')
appbuilder.add_view(QuanLyDonXinNghiView, "Quản lý Đơn Xin Nghỉ", category='Công việc')



db.create_all()
