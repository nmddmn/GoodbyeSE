from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATE, FLOAT, BOOLEAN
from sqlalchemy.orm import relationship

class DonXinNghiModel(Model):
    __tablename__ = "DonXinNghi"
    MADONXINNGHI = Column(INT, primary_key=True)
    LYDO = Column(VARCHAR(255), nullable=False)
    TRANGTHAI = Column(BOOLEAN, default=False)
    THOIGIANGUI = Column(DATE, nullable=False)
    MALAMVIEC = Column(INT, ForeignKey('LamViec.MALAMVIEC'), nullable=False)
    MANHANVIEN = Column(INT, ForeignKey('NhanVien.MANHANVIEN'), nullable=False)
    
    LamViec = relationship("LamViecModel")
    NhanVien = relationship("NhanVienModel")

    def __repr__(self):
        return str(self.MADONXINNGHI)