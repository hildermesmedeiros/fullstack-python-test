# -*- coding: utf-8 -*-
from typing import List, Dict
import mysql.connector
import time
#I instanciated bycrypt in the init /backEnd folder
from backEnd import bcrypt 
from backEnd.models import tm_siteuser
from backEnd import app, db 
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
        except Exception as e1:
            db.session.rollback()
            commiterror = e1
            print("Commit Error:", e1)
    except Exception as e2:
        otherError = e2
        print('Other error: ', e2)
        return
    finally:
        if commiterror == None and otherError == None:
            print('Usuário adicionado: ', User.username )
        else:
            print('O erro acima fechou o programa')                          
