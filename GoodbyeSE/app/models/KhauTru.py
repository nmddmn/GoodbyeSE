from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME, FLOAT
from sqlalchemy.orm import relationship

class KhauTruModel(Model):
    __tablename__ = "KhauTru"
    MAKHAUTRU = Column(INT, primary_key=True)
    TENKHAUTRU = Column(VARCHAR(20), nullable=False)
    SOTIEN = Column(INT, nullable=False)

    def __repr__(self):
        return self.TENKHAUTRU