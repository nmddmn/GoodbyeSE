from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME, FLOAT, BOOLEAN
from sqlalchemy.orm import relationship

class LamViecModel(Model):
    __tablename__ = "LamViec"
    MALAMVIEC = Column(INT, primary_key=True)
    MANHANVIEN = Column(VARCHAR(20), ForeignKey('NhanVien.MANHANVIEN'), nullable=False)
    MALICHLAM = Column(INT, ForeignKey('LichLam.MALICHLAM'), nullable=False)
    DIEMDANH = Column(BOOLEAN, nullable=False)
    VITRI = Column(VARCHAR(20), nullable=False)

    def __repr__(self):
        return self.name