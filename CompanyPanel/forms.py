from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

"""For fileupload you need to import below form fields"""
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

class EmployeeRegister(FlaskForm):
    emp_name = StringField("emp_name", validators=[DataRequired()])
    emp_id = StringField("emp_id", validators=[DataRequired()])
    emp_des = StringField("emp_des", validators=[DataRequired()])
    emp_photo = FileField("emp_photo", validators=[FileRequired()])
    submit = SubmitField("Register")