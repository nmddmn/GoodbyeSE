from flask_appbuilder import Model
from sqlalchemy import Column, INT, ForeignKey, VARCHAR, DATETIME, DATE
from sqlalchemy.orm import relationship
from flask_appbuilder.fieldwidgets import DateTimePickerWidget
from flask_appbuilder.security.sqla.models import User

class NhanVienModel(Model):
    __tablename__ = "NhanVien"
    MANHANVIEN = Column(INT, primary_key=True)
    HOTEN = Column(VARCHAR(45), nullable=False)
    GIOITINH = Column(VARCHAR(10), nullable=False)
    NGAYSINH = Column(DATE(), nullable=False)
    DIACHI = Column(VARCHAR(255), nullable=False)
    CCCD = Column(VARCHAR(20), nullable=False, unique = True)
    SDT = Column(VARCHAR(20), nullable=False, unique = True)
    VITRICONGVIEC = Column(VARCHAR(20), nullable=False)
    NGAYBATDAU = Column(DATE(), nullable=False)
    TAIKHOAN = Column(INT, ForeignKey('ab_user.id'), nullable=False)
    
    taikhoan = relationship("User")
    
    def __repr__(self):
        return self.HOTEN