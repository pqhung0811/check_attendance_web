from project import app
from flask import jsonify, request
from project.service.departmentService import DepartmentService

@app.route('/api/departments', methods=['GET'])
def getDepartmentsRouter():
    departments = DepartmentService.getAllDepartments()
    departmentList = [{'id': department.id, 'name': department.name} for department in departments]
    return jsonify(departmentList)

@app.route('/api/department/<id>', methods=['GET'])
def getDepartmentByIdRouter(id):
    department = DepartmentService.getDepartmentById(id)
    if department:
        return jsonify({'id': department.id, 'name': department.name})
    else:
        return jsonify({"message": "Department not found"}), 404
    