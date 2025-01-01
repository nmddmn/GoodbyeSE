from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME, FLOAT
from sqlalchemy.orm import relationship

class LuongPhuCapModel(Model):
    __tablename__ = "LuongPhuCap"
    MATHONGTINLUONG = Column(INT, ForeignKey('LuongNhanVien.MATHONGTINLUONG'), primary_key=True)
    MAPHUCAP = Column(INT, ForeignKey('PhuCap.MAPHUCAP'), primary_key=True)
    
    def __repr__(self):
        return self.name