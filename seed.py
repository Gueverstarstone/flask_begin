# Instead of starting with an empty database, you insert default or sample records that the application needs to run or test properly.
from faker import Faker

from app import app, db, User

with app.app_context():

    # Create and initialize a faker generator
    fake = Faker()

    #delete all rows in the users table
    User.query.delete()

    #create an empty list
    many_users=[]

    # Add some User instances to the list
    for n in range(10):
        user = User(
            name=fake.name(), 
            email=fake.unique.email(), # ensures no duplicate emails
            years_old=fake.random_int(min=18, max=60)
        ) 
        many_users.append(user)



    # Insert each User in the list into the database table
    db.session.add_all(many_users)

    # Commit the transaction
    db.session.commit()