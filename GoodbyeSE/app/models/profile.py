from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, VARCHAR, DATETIME
from sqlalchemy.orm import relationship

class EmployeeProfileModel(Model):
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45), nullable=False)
    gender = Column(VARCHAR(10), nullable=False)
    date_of_birth = Column(DATETIME, nullable=False)
    address = Column(VARCHAR(225), nullable=False)
    citizen_id = Column(VARCHAR(20), unique = True, nullable=False)
    phone_number = Column(VARCHAR(20), unique = True, nullable=False)
    job_position = Column(VARCHAR(20), nullable=False)
    start_date = Column(DATETIME, nullable=False)
    user_id = Column(Integer, ForeignKey('ab_user.id'), nullable=False)
    
    def __repr__(self):
        return self.name