from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME, FLOAT, BOOLEAN
from sqlalchemy.orm import relationship
from app.models.LichLam import LichLamModel

class LamViecModel(Model):
    __tablename__ = "LamViec"
    MALAMVIEC = Column(INT, primary_key=True)
    MANHANVIEN = Column(INT, ForeignKey('NhanVien.MANHANVIEN'), nullable=False)
    MALICHLAM = Column(INT, ForeignKey('LichLam.MALICHLAM'), nullable=False)
    DIEMDANH = Column(BOOLEAN, default=False)
    VITRI = Column(VARCHAR(20), nullable=False)
    
    NhanVien = relationship("NhanVienModel")
    LichLam = relationship("LichLamModel")

    def __repr__(self):
        return f'{self.MALAMVIEC} : {self.MANHANVIEN} : {self.LichLam.THOIGIAN}'