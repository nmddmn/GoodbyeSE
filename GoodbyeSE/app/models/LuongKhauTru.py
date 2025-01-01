from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME, FLOAT
from sqlalchemy.orm import relationship

class LuongKhauTruModel(Model):
    __tablename__ = "LuongKhauTru"
    MATHONGTINLUONG = Column(INT, ForeignKey('LuongNhanVien.MATHONGTINLUONG'), primary_key=True)
    MAKHAUTRU = Column(INT, ForeignKey('KhauTru.MAKHAUTRU'), primary_key=True)

    def __repr__(self):
        return self.name