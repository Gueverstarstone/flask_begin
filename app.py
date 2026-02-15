# Import necessary modules

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI using the environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Disable SQLAlchemy modification tracking for better performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Initialize Flask-Migrate with the Flask app and SQLAlchemy instance
migrate = Migrate(app, db)

# define user model
class User(db.Model):
    __tablename__ = 'users' # explicitly set table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    years_old = db.Column(db.Integer)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    department = db.relationship('Department', backref='users')

    def __repr__(self):
        return f"<User {self.id}, {self.name}, {self.email}, {self.years_old}>"

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)

    def __repr__(self):
        return f'<Department {self.id}, {self.name}, {self.address}>'