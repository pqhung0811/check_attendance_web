from project import app
from flask import jsonify, request
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

@app.route('/api/employee/register/username', methods=['POST'])
def regiter():
    data = request.json
    
    username = data.get('username')

    employee = EmployeeService.getEmployeeByUsername(username)
    if employee:
        return jsonify({"message": "username is available"})
    else:
        return jsonify({"message": "username exists"}), 401
