from flask import render_template, redirect, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, AppBuilder, expose, has_access
from app.models.LichLam import LichLamModel
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from .utils import *
from flask_appbuilder.exceptions import FABException
import io
from flask import send_file
from openpyxl import Workbook
from app import db

class LichLamView(ModelView):
    datamodel = SQLAInterface(LichLamModel)
    list_columns = ['MALICHLAM', 'NAM', 'TUAN', 'THU', 'THOIGIAN']
    
    list_title = "Lịch Làm"
    
    route_base = "/lich_lam"
    
    @expose("/list/")
    @has_access
    def list(self):
        self.update_redirect()
        try:
            widgets = self._list()
        except FABException as exc:
            flash(f"An error occurred: {exc}", "warning")
            return redirect(self.get_redirect())
        return self.render_template(
            "custom_list.html", title=self.list_title, widgets=widgets
        )
        
    
    @expose("/export_excel/")
    @has_access
    def export_excel(self):
        # Query the data
        records = db.session.query(LichLamModel).all()

        # Create an Excel file
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Your Model Data"

        # Add header
        sheet.append(['MALICHLAM', 'NAM', 'TUAN', 'THU', 'THOIGIAN'])

        # Add rows
        for record in records:
            sheet.append([record.MALICHLAM, record.NAM, record.TUAN, record.THU, record.THOIGIAN])

        # Save to a BytesIO buffer
        output = io.BytesIO()
        workbook.save(output)
        output.seek(0)

        # Send the file
        return send_file(
            output,
            as_attachment=True,
            download_name="your_model.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )