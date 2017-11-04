import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///users.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

<<<<<<< HEAD
#first term determines user type (not shown here)
user = User("student", "admin", "password", "Atharva", "Bhat", "2404900575", "abhat98@gmail.com", "My name is Atharva!")
>>>>>>> 89bba69c17178427a535998cd9f62c7e09adde39
session.add(user)

user = User("student", "user1", "password", "John", "Doe", "2404900575", "abhat98@gmail.com" , "My name is John!")
session.add(user)

user = User("student", "user2", "password", "Jane", "Doe", "2404900575", "abhat98@gmail.com", "My name is Jane!")
session.add(user)


nominator = Nominator("nominator", "nom1", "password", "Dylan", "Fox", "dfox@gmail.com", {"Academic" : True, "Arts" : False, "Athletics" : True, "STEM": True, "Service" : False })
session.add(nominator)

nominator = Nominator("nominator", "nom2", "password", "Mike", "Williams", "mikewill@gmail.com", {"Academic" : True, "Arts" : False, "Athletics" : True, "STEM": True, "Service" : False })
session.add(nominator)


# commit the record the database
session.commit()
session.commit()
