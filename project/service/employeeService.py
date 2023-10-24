from project.model.employee import Employee
from project import db

class EmployeeService(object):
    @staticmethod
    def getAllEmployees():
        employees = Employee.query.all()
        return employees
    
    @staticmethod
    def getEmployeeById(id):
        employee = Employee.query.get(id)
        return employee
    
    @staticmethod
    def getEmployeeByUsernamePassword(username, password):
        employee = Employee.query.filter_by(username=username, password=password).first()
        return employee
    
    @staticmethod
    def addNewEmployee(username, password):
        employee = Employee(username=username, password=password)
        db.session.add(employee)
        db.session.commit()
        return
    
    @staticmethod
    def updateEmployeeInfomation():
        db.session.commit()
        return

    @staticmethod
    def checkUsernameExist(username):
        employeeExists = Employee.query.filter_by(username=username).exists()
        
        return db.session.query(employeeExists).scalar()
    
    @staticmethod
    def checkEmailExist(email):
        employeeExists = Employee.query.filter_by(email=email)
        
        return db.session.query(employeeExists).scalar()



