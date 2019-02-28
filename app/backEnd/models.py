# -*- coding: utf-8 -*-
#I could have used flask userMixin but explicit doing it, to me, that
#never did it try flask, it would require better understanding of it
#from flask_login import UserMixin
from backEnd import db
#I instanciated bcrypt in the init /backEnd folder
from backEnd import bcrypt
import time
#http://flask-sqlalchemy.pocoo.org/2.3/models/
#db.Model is main class from sqlalchemy
class tm_siteuser(db.Model):
    
    __tablename__ = "tm_siteuser"
    __table_args__ = {'mysql_engine':'InnoDB','mysql_charset':'utf8'}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),unique=True)
    firstname = db.Column(db.Text, nullable=False)
    middlename = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    t1 = db.Column(db.DateTime, nullable=False, onupdate=time.strftime('%Y-%m-%d %H-%M-%S'))
    hashpass = db.Column(db.String(128), nullable=False)
    typeid = db.Column(db.Integer)
    
    def __init__(self, username, firstname, middlename, email, birthday, t1, hashpass, typeid):
        self.username = str.lower(username)
        self.firstname = firstname
        self.middlename = middlename
        self.email = email
        self.birthday = birthday
        self.t1 = t1
        self.hashpass = bcrypt.generate_password_hash(hashpass).decode('utf-8')
        self.typeid = typeid
    #flask_login recommends this 4 methods    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
        
    def is_anonymous(self):
        return False
        
    def get_id(self):
    #in python3 unicode = str
        return str(self.id)
    
    def __repr__(self):
        return '<username - {}>'.format(self.username)   
            
