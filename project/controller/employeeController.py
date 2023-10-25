from project import app
from flask import jsonify, request, Blueprint
from project.model.employee import Employee
from project.service.employeeService import EmployeeService

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
        
@app.route('/api/employee/update/<int:id>', methods=['PUT'])
def updateInfomation(id):
    data = request.json
    
    employee = EmployeeService.getEmployeeById(id=id)
    employee.fullname = data.get('fullname', employee.fullname)
    employee.phoneNumber = data.get('phoneNumber',employee.phoneNumber)
    employee.email = data.get('email', employee.email)
    employee.dateOfBirth = data.get('dateOfBirth', employee.dateOfBirth)
    employee.departmentId = data.get('departmentId', employee.departmentId)

    EmployeeService.updateEmployeeInfomation()
    return jsonify({"message": "update successflly"})
