from project import db

class Department(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name


