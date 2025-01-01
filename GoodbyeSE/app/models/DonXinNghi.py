from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, INT, VARCHAR, DATETIME, FLOAT, BOOLEAN
from sqlalchemy.orm import relationship

class DonXinNghiModel(Model):
    __tablename__ = "DonXinNghi"
    MADONXINNGHI = Column(INT, primary_key=True)
    LYDO = Column(VARCHAR(255), nullable=False)
    TRANGTHAI = Column(BOOLEAN, nullable=False)
    THOIGIANGUI = Column(DATETIME, nullable=False)
    MALAMVIEC = Column(INT, ForeignKey('LamViec.MALAMVIEC'), nullable=False)

    def __repr__(self):
        return self.name