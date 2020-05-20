"""
    Project Archive Using Flask
    -----------------------------
    Author Anwesh Dahal
"""

# importing the flask module
from flask import Flask
# importing the flask sql alchemy module
from flask_sqlalchemy import SQLAlchemy

# assigning the name of the module to the variable app
app = Flask(__name__)
# an anti CRSF key to avoid CRSF attack
app.config['SECRET_KEY'] = 'f58cfdba2ad20fc6da81e81eb64647cb'
# Setting the reference to the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
from main import routes

