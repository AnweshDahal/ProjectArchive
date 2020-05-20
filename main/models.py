from main import db
from datetime import datetime
# Project name, date posted, version, language, script, markup, style, github
class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50), nullable=False)
    date_published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    version = db.Column(db.String(20), nullable=False) 
    language = db.Column(db.String(25), default="")
    dependency = db.Column(db.String(25), default="")
    script = db.Column(db.String(25), default="")
    markup = db.Column(db.String(25), default="")
    style = db.Column(db.String(25), default="")
    github = db.Column(db.String(50), nullable=False)
    programming_lang = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'ID: {self.id}, Project Name: {self.project_name}, '
