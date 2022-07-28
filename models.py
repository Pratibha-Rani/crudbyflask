from sqlalchemy import String, Integer, DateTime
import datetime
from app import db
class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key = True)
    employee_name = db. Column(db.String(100), nullable = False)
    employee_design = db.Column(db.String(100), nullable = False)
    employee_age = db.Column(db.Integer(), nullable = False)
    employee_description = db.Column(db.String(100), nullable = False)


    def __repr__(self):
        return "<Employee %r>" % self.employee_name