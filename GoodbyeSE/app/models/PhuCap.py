from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME, FLOAT
from sqlalchemy.orm import relationship

class PhuCapModel(Model):
    __tablename__ = "PhuCap"
    MAPHUCAP = Column(INT, primary_key=True)
    TENPHUCAP = Column(VARCHAR(20), nullable=False)
    SOTIEN = Column(INT, nullable=False)

    def __repr__(self):
        return self.name