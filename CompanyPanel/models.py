from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(), index=True)
    emp_id = db.Column(db.String(), unique=True, index=True)
    emp_des = db.Column(db.String(), index=True)
    emp_photo = db.Column(db.String(), unique=True)
