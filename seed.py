# Instead of starting with an empty database, you insert default or sample records that the application needs to run or test properly.

from app import app, db, User

with app.app_context():

    #delete all rows in the users table
    User.query.delete()

    #create an empty list
    many_users=[]

    # Add some User instances to the list
    many_users.append(User(name = "Joe",email = "joe@gmail.com",years_old = 34 ))
    many_users.append(User(name = "Fred",email = "fred@gmail.com",years_old = 22 ))
    many_users.append(User(name = "Kinuthia",email = "kinuthia@gmail.com",years_old = 29 ))
    many_users.append(User(name = "Sifuna",email = "sifuna@gmail.com",years_old = 45 ))


    # Insert each User in the list into the database table
    db.session.add_all(many_users)

    # Commit the transaction
    db.session.commit()