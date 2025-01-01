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

from app.views.NhanVien import NhanVienView
appbuilder.add_view(NhanVienView, "Thông Tin Nhân Viên", category='Thông Tin Nhân Viên')

from app.views.LuongNhanVien import LuongNhanVienView
from app.views.Luong import LuongView
from app.views.PhuCap import PhuCapView
from app.views.LuongPhuCap import LuongPhuCapView
from app.views.KhauTru import KhauTruView
from app.views.LuongKhauTru import LuongKhauTruView

appbuilder.add_view(LuongNhanVienView, "Luong Nhan Vien", category='Lương')
appbuilder.add_view(LuongView, "Luong", category='Lương')
# appbuilder.add_separator("Lương")
appbuilder.add_view(PhuCapView, "Phu Cap", category='Lương')
appbuilder.add_view(LuongPhuCapView, "Luong Phu Cap", category='Lương')
# appbuilder.add_separator("Lương")
appbuilder.add_view(KhauTruView, "Khau Tru", category='Lương')
appbuilder.add_view(LuongKhauTruView, "Luong Khau Tru", category='Lương')

from app.views.LamViec import LamViecView
from app.views.LichLam import LichLamView
from app.views.DonXinNghi import DonXinNghiView

appbuilder.add_view(LamViecView, "Lam Viec", category='Công việc')
appbuilder.add_view(LichLamView, "Lich Lam", category='Công việc')
appbuilder.add_view(DonXinNghiView, "Don Xin Nghi", category='Công việc')


db.create_all()
