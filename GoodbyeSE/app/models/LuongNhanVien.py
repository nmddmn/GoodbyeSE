from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME
from sqlalchemy.orm import relationship

class LuongNhanVienModel(Model):
    __tablename__ = "LuongNhanVien"
    MATHONGTINLUONG = Column(INT, primary_key=True)
    MALOAILUONG = Column(INT, ForeignKey('Luong.MALOAILUONG'), nullable=False)
    MANHANVIEN = Column(VARCHAR(20), ForeignKey('NhanVien.MANHANVIEN'), nullable=False)
    THANG = Column(INT, nullable=False)
    NAM = Column(INT, nullable=False)
    SONGAYLAM = Column(INT, nullable=False)
    SONGAYVANG = Column(INT, nullable=False)
    LUONGNHAN = Column(INT, nullable=False)

    def __repr__(self):
        return self.name