# -*- coding: utf-8 -*-
from backEnd import db
import time
#http://flask-sqlalchemy.pocoo.org/2.3/models/
#db.Model is main class from sqlalchemy
class tm_siteuser(db.Model):
    
    __tablename__ = "tm_siteuser"
    __table_args__ = {'mysql_engine':'InnoDB','mysql_charset':'utf8'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(100),unique=True)
    firstname = db.Column(db.Text, nullable=False)
    middlename = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    t1 = db.Column(db.DateTime, nullable=False, onupdate=time.strftime('%Y-%m-%d %H-%M-%S'))
    hashpass = db.Column(db.String(128), nullable=False)
    typeid = db.Column(db.Integer)
    
    def __init__(self, username, firstname, middlename, email, birthday, t1, hashpass, typeid):
        self.username = username
        self.firstname = firstname
        self.middlename = middlename
        self.email = email
        self.birthday = birthday
        self.t1 = t1
        self.hashpass = hashpass
        self.typeid = typeid
