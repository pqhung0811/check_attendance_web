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
    def addNewEmployee(username, password, email, phoneNumber):
        employee = Employee(username=username, password=password, email=email, phoneNumber=phoneNumber)
        db.session.add(employee)
        return
    
    @staticmethod
    def checkUsernameExist(username):
        employeeExists = Employee.query.filter_by(username=username).exists()
        
        return db.session.query(employeeExists).scalar()
    
    @staticmethod
    def checkEmailExist(email):
        employeeExists = Employee.query.filter_by(email=email)
        
        return db.session.query(employeeExists).scalar()

    """description of class"""


