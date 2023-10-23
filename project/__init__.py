"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from waitress import serve

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/CV/CV/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)

import project.views
import project.controller.departmentController
import project.controller.employeeController
from project.model.department import Department
from project.model.employee import Employee
