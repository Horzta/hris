from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relation
from common.containers import Databases

Base = Databases.default_conn().base


class Account(Base):
    __tablename__ = 'account'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    phone_number = Column('phone_number', String(45))



class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(16))
    email = Column('email', String(32))
    password = Column('password', String(32))



class Employee(Base):
    __tablename__ = 'employee'

    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(100))
    middle_name = Column('middle_name', String(100))
    last_name = Column('last_name', String(100))
    contact_number = Column('contact_number', String(50))
    e_mail = Column('email', String(45))
    gender = Column('gender', String(1))
    account_id = Column(Integer, ForeignKey('account.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    account = relation('Account')
    user = relation('User')
