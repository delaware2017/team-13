from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///users.db', echo=True)

Base = declarative_base()


########################################################################
class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_type = Column(String)
    username = Column(String)
    password = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    phoneNumber = Column(String)
    email = Column(String)
    personalStatement = Column(String)


    #----------------------------------------------------------------------
    def __init__(self, user_type, username, password, firstName, lastName, phoneNumber, email, personalStatement):
        """"""
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.email = email
        self.personalStatement = personalStatement


class Nominator(Base):
    """"""
    __tablename__ = "nominators"

    id = Column(Integer, primary_key=True)
    user_type = Column(String)
    username = Column(String)
    password = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)

    studentFirstName = Column(String)
    studentLastName = Column(String)
    # categories = {"Academic" : True, "Arts" : False, "Athletics" : True, "STEM": True, "Service" : False }


    #----------------------------------------------------------------------
    def __init__(self, user_type, username, password, firstName, lastName, email, categories):
        """"""
        self.username = username
        self.user_type = user_type
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.categories = categories


# create tables
Base.metadata.create_all(engine)
