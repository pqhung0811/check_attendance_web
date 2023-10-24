from sqlalchemy import Null
from project import app
from flask import jsonify, request
from project.model.employee import Employee
from project.service.employeeService import EmployeeService

theEmployee = Null

@app.route('/api/employee/<id>', methods=['GET'])
def getEmployeeByIdRouter(id):
    employee = EmployeeService.getEmployeeById(id)
    if employee:
        return jsonify({'id': employee.id, 'fullname': employee.fullname})
    else:
        return jsonify({"message": "Can not find"}), 401

@app.route('/api/employee/login', methods=['POST'])
def login():
    data = request.json
    
    username = data.get('username')
    password = data.get('password')

    employee = EmployeeService.getEmployeeByUsernamePassword(username, password)
    theEmployee = employee
    if employee:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid login credentials"}), 401

@app.route('/api/employee/register', methods=['POST'])
def Register():
    data = request.json
    
    username = data.get('username')
    password = data.get('password')

    checkUser = EmployeeService.checkUsernameExist(username=username)
    if checkUser==False:
        EmployeeService.addNewEmployee(username=username, password=password)
        return jsonify({"message": "register successflly"})
    else:
        return jsonify({"message": "username exists"}), 401
        
@app.route('/api/employee/register/update', methods=['POST'])
def updateInfomation():
    data = request.json
        
    theEmployee.fullname = data.get('fullname')
    theEmployee.phoneNumber = data.get('phoneNumber')
    theEmployee.email = data.get('email')
    theEmployee.dateOfBirth = data.get('dateOfBirth')
    theEmployee.departmentId = data.get('departmentId')

    EmployeeService.updateEmployeeInfomation()
    return jsonify({"message": "update successflly"})
