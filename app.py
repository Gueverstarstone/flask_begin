# Import necessary modules

from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from sqlalchemy_serializer import SerializerMixin

# load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI using the environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Disable SQLAlchemy modification tracking for better performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Initialize Flask-Migrate with the Flask app and SQLAlchemy instance
migrate = Migrate(app, db)


@app.route('/')
def index():
    body = {'message':'Welcome to the user directory'}
    return make_response(body, 200)

# @app.route('/users/<int:id>')
# def user_by_id(id):
#     user = User.query.filter(User.id == id).first()

#     if user:
#         response_body = f'<p>{user.name}</p>'
#         response_status = 200
#     else:
#         response_body = f'<p>User {id} not found</p>'
#         response_status = 404

#     response = make_response(response_body, response_status)
#     return response

@app.route('/demo_json')
def demo_json():
    user = User.query.first()
    user_dict = {'id': user.id, 
                'name' : user.name, 
                'email' : user.email
                }
    return make_response(user_dict,200)

@app.route('/users/<int:id>')
def user_by_id(id):
    user = User.query.filter(User.id == id).first()

    if user:
        body = user.to_dict()
        status = 200
    else:
        body = {'message': f'User {id} not found.'}
        status = 404
        
    return make_response(body, status)

@app.route('/users/startswith/<string:letter>')
def users_starting_with(letter):
    # Query all users whose names start with the given letter
    users = User.query.filter(User.name.like(f"{letter}%")).all()

    # Use .to_dict() instead of manually building dicts
    users_dicts = [user.to_dict() for user in users]

    body = {
        'count': len(users_dicts),
        'users': users_dicts
    }
    return make_response(body, 200)
    

# define user model
class User(db.Model, SerializerMixin):
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