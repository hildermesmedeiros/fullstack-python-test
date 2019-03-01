# -*- coding: utf-8 -*-
from typing import List, Dict
import mysql.connector
import time
#I instanciated bycrypt in the init /backEnd folder
from backEnd import bcrypt 
from backEnd.models import tm_siteuser
from backEnd import app, db 
from sqlalchemy import exc
#import datetime

    
#To be used in signup    
def add_user(username, firstname, middlename, email, birthday, password, usertype):
    try:
        commiterror= None
        otherError = None
        User = tm_siteuser(
            username =  str.lower(username),
            firstname = firstname,
            middlename = middlename,
            email = email,
            birthday = birthday,
            #first add requires first time stamp
            t1 = time.strftime('%Y-%m-%d %H-%M-%S'),
            hashpass = password,
            typeid = usertype
        )    
        db.session.add(User)
        try:
            db.session.commit()
        except exc.SQLAlchemyError as e1:
            commiterror = e1
            db.session.rollback()
            print("Commit Error:", e1.args[0])
            print("Commit failed, roll back done")
    except Exception as e2:
        otherError = e2
        print('Other error: ', e2)
    finally:
        if commiterror == None and otherError == None:
            print('Usuário adicionado: ', User.username )
                          
