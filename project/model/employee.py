from project import db


class Employee(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    fullname = db.Column(db.String(80))
    dateOfBirth = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(11), unique=True, nullable=False)
    departmentId = db.Column(db.Integer, db.ForeignKey("department.id"))

    def __init__(self, username, password, fullname, dateOfBirth, email, phoneNumber, departmentId):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.phoneNumber = phoneNumber
        self.departmentId = departmentId
