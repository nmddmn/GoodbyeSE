import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

from app.views.custom_index import CustomIndexView

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview = CustomIndexView)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from app.views import *
from app.views.employee.profile import *
from app.views.employer.profile import *

appbuilder.add_view(EmployeeProfileView, "Profile", category='Employee')
appbuilder.add_separator("Employee")
appbuilder.add_view(EmployerProfileView, "Profile", category='Employer')

db.create_all()
