from flask_appbuilder import Model
from sqlalchemy import Column, INT, ForeignKey, VARCHAR, DATETIME
from sqlalchemy.orm import relationship

class NhanVienModel(Model):
    __tablename__ = "NhanVien"
    MANHANVIEN = Column(VARCHAR(10), primary_key=True)
    HOTEN = Column(VARCHAR(45), nullable=False)
    GIOITINH = Column(VARCHAR(10), nullable=False)
    NGAYSINH = Column(DATETIME(), nullable=False)
    DIACHI = Column(VARCHAR(255), nullable=False)
    CCCD = Column(VARCHAR(20), nullable=False, unique = True)
    SDT = Column(VARCHAR(20), nullable=False, unique = True)
    VITRICONGVIEC = Column(VARCHAR(20), nullable=False)
    NGAYBATDAU = Column(DATETIME(), nullable=False)
    TAIKHOAN = Column(INT, ForeignKey('ab_user.id'), nullable=False)
    
    def __repr__(self):
        return self.name