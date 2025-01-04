from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME, Table
from sqlalchemy.orm import relationship
from app.models.PhuCap import PhuCapModel
from app.models.KhauTru import KhauTruModel
from app.models.Luong import LuongModel

LuongPhuCapTable = Table('LuongNhanVien_PhuCap', Model.metadata,
     Column('LuongNhanVien_MATHONGTINLUONG', INT, ForeignKey('LuongNhanVien.MATHONGTINLUONG'), primary_key=True),
     Column('PhuCap_MAPHUCAP', INT, ForeignKey('PhuCap.MAPHUCAP'), primary_key=True)
    )

LuongKhauTruTable = Table('LuongNhanVien_KhauTru', Model.metadata,
     Column('LuongNhanVien_MATHONGTINLUONG', INT, ForeignKey('LuongNhanVien.MATHONGTINLUONG'), primary_key=True),
     Column('KhauTru_MAKHAUTRU', INT, ForeignKey('KhauTru.MAKHAUTRU'), primary_key=True)
    )


class LuongNhanVienModel(Model):
    __tablename__ = "LuongNhanVien"
    MATHONGTINLUONG = Column(INT, primary_key=True)
    MALOAILUONG = Column(INT, ForeignKey('Luong.MALOAILUONG'), nullable=False)
    MANHANVIEN = Column(INT, ForeignKey('NhanVien.MANHANVIEN'), nullable=False)
    THANG = Column(INT)
    NAM = Column(INT)
    SONGAYLAM = Column(INT, nullable=False)
    SONGAYVANG = Column(INT, nullable=False)
    LUONGNHAN = Column(INT)
    
    NhanVien = relationship("NhanVienModel")
    Luong = relationship("LuongModel")
    PhuCap = relationship("PhuCapModel", secondary=LuongPhuCapTable)
    KhauTru = relationship("KhauTruModel", secondary=LuongKhauTruTable)

    def __repr__(self):
        return f'{self.MATHONGTINLUONG} : {self.MANHANVIEN}'