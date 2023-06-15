from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import EmployeeRegister
from .models import Employee, db
import os


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

"""Allowed File Function"""
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
"""filename adding using empId"""
def new_filename(name, old_name_extension):
    return name+"."+old_name_extension.split(".")[1]
""""""

admin_bp = Blueprint("admin_bp", __name__,
                     template_folder="templates",
                     static_folder="static",
                     static_url_path="/CompanyPanel/static")

@admin_bp.route("/")
def index():
    emp = db.session.execute(db.select(Employee)).scalars()
    return render_template("index.html", emp=emp)

@admin_bp.route("/register", methods=["GET", "POST"])
def register():
    form = EmployeeRegister()
    if form.validate_on_submit():
        file = form.emp_photo.data
        employee = Employee(emp_name=form.emp_name.data,
                            emp_id=form.emp_id.data,
                            emp_des=form.emp_des.data,
                            emp_photo=new_filename(form.emp_id.data, form.emp_photo.data.filename))
        #print(form.emp_photo.data.filename)
        #print(new_filename(form.emp_id.data, form.emp_photo.data.filename))
        #print(file)
        file.save(os.path.join("CompanyPanel/static/uploads/", new_filename(form.emp_id.data, form.emp_photo.data.filename)))
        db.session.add(employee)
        db.session.commit()
        flash("Created Successfully!!")
        return redirect(url_for('admin_bp.index'))
    return render_template("register.html", form=form)