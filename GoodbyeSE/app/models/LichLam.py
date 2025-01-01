from flask_appbuilder import Model
from sqlalchemy import Column, INT, DATETIME
from sqlalchemy.orm import relationship

class LichLamModel(Model):
    __tablename__ = "LichLam"
    MALICHLAM = Column(INT, primary_key=True)
    NAM = Column(INT, nullable=False)
    TUAN = Column(INT, nullable=False)
    THU = Column(INT, nullable=False)
    THOIGIAN = Column(DATETIME, nullable=False)


    def __repr__(self):
        return self.name