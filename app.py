from flask import Flask,jsonify,request
from sqlalchemy import String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app= Flask(__name__)
IS_DEV = app.env == 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://pratibha:1234abc@localhost/employee'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class employee(db.Model):
    __tablename__ = 'employee'
    employee_id = db.Column(db.Integer, primary_key = True)
    employee_name = db. Column(db.String(100), nullable = False)
    employee_address = db.Column(db.String(100), nullable = False)
    employee_age = db.Column(db.Integer(), nullable = False)
    employee_description = db.Column(db.String(100), nullable = False)

    def __init__(self,employee_name,employee_address,employee_age,employee_description):
        self.employee_name=employee_name
        self.employee_address=employee_address
        self.employee_age=employee_age
        self.employee_description=employee_description


    def __repr__(self):
        return f"<employee{self.employee_name}>"

@app.route('/')
def index():
    return jsonify({"message":"Welcome to my  Employee site"})
    

@app.route('/employees', methods = ['POST','GET'])
def create_employee():
    if request.method=='POST':
        if request.is_json:
            data=request.get_json()
            new_employee= employee(employee_name = data['employee_name'],
            employee_address =data['employee_address'],
            employee_age = data['employee_age'],
            employee_description  = data ['employee_description'],)
            db.session.add(new_employee)
            db.session.commit()
            return{"message": f"Employee {new_employee.employee_name} has been created successfully."}
        else:
            return{"error":"The request is not available in JSON format"     }
            
    elif request.method=='GET':
        employees=employee.query.all()
        results=[
            {
            "employee_name":Employee.employee_name,
            "employee_address":Employee.employee_address,
            "employee_age":Employee.employee_age,
            "employee_description":Employee.employee_description
        } for Employee in employees ]
        return{"count":len(results),"employees":results}

@app.route('/employees/<employee_id>', methods = ['GET','PUT','DELETE'])
def employee_by_id(employee_id):
    Employee=employee.query.get_or_404(employee_id)

    if request.method=='GET':
        response={
            "employee_name":Employee.employee_name,
            "employee_address":Employee.employee_address,
            "employee_age":Employee.employee_age,
            "employee_description":Employee.employee_description,
        }
        return{"message":"success", "Employee": response}
    elif request.method=='PUT':
        data= request.get_json()
        Employee.employee_name = data['employee_name']
        Employee.employee_address =data['employee_address']
        Employee.employee_age = data['employee_age']
        Employee.employee_description  = data ['employee_description']
        db.session.add(Employee)
        db.session.commit()
        return {"message": f"Employee {Employee.employee_name} successfully updated"}
    elif request.method == 'DELETE':
        db.session.delete(Employee)
        db.session.commit()
        return {"message": f"Employee {Employee.employee_name} successfully deleted."}

if __name__ =='__main__':

    app.run(debug=True) 
   
