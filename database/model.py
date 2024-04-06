from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import insert,select

#from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///trial.db")

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True,nullable=False)
    productname = Column(String,nullable=False)
    unitprice = Column(Integer,nullable=False)
    quantity = Column(Integer)

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer,nullable=False)
    firstname = Column(String,nullable=False)
    lastname = Column(String,nullable=False)
    gender = Column(String,nullable=False)
    email = Column(String,primary_key=True,nullable=False)
    password = Column(String,nullable=False)
    phone = Column(String)
    access = Column(String)

    def all(self):
        return (self.id,self.firstname,self.lastname,self.email,self.phone)
    def Admin_all(self):
        return (self.id,self.firstname,self.lastname,self.email,self.password,self.phone,self.access)
Session = sessionmaker()
Session.configure(bind = engine)
session = Session()