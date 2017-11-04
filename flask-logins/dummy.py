import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///users.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password", "Atharva", "Bhat", "2404900575", "abhat98@gmail.com", "My name is Atharva!")
session.add(user)

user = User("user1","password", "John", "Doe", "2404900575", "abhat98@gmail.com" , "My name is John!")
session.add(user)

user = User("user2","password", "Jane", "Doe", "2404900575", "abhat98@gmail.com", "My name is Jane!")
session.add(user)

# commit the record the database
session.commit()
session.commit()
