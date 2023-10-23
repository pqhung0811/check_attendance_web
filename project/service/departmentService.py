from project import db
from project.model.department import Department

class DepartmentService:
    @staticmethod
    def getAllDepartments():
        departments = Department.query.all()
        return departments
    
    @staticmethod
    def getDepartmentById(id):
        department = Department.query.get(id)
        return department
