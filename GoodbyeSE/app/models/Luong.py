from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME, FLOAT
from sqlalchemy.orm import relationship

class LuongModel(Model):
    __tablename__ = "Luong"
    MALOAILUONG = Column(INT, primary_key=True)
    TENLOAILUONG = Column(VARCHAR(20), nullable=False)
    VITRI = Column(VARCHAR(20), nullable=False)
    HESOLUONG = Column(FLOAT, nullable=False)
    LUONGCOBAN = Column(INT, nullable=False)


    def __repr__(self):
        return f'{self.MALOAILUONG} : {self.TENLOAILUONG}'