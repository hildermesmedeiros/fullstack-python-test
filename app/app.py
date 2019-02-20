from typing import List, Dict
from flask import Flask, request, render_template, json
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
#from itsdangerous import (TimedJSONWebSignatureSerializeras Serializer, BadSignature, SignatureExpired)
from werkzeug.security import generate_password_hash, check_password_hash
import time  
import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DoNoEVERshareittosomeone'
auth = HTTPBasicAuth()

def gettingUsers() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'telemedicina'
    }
    connection = mysql.connector.connect(**config)
#python postgresql connection
    cursor = connection.cursor()
#Selecting all users
    cursor.execute('SELECT uname,hashpass FROM tm_siteuser')
#fetchin data  all data from user   
#    data=cursor.fetchone()
    users = []
    for row in cursor:
        a = list(row)
        dic = {'username': a[0], 'password': a[1]}
        users.append(dic)
#closing the table connection
    cursor.close()
#closing the db connection
    connection.close()
    return users

def add_hildermes():
#    try:
    config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'telemedicina'
    }
    
    connection = mysql.connector.connect(**config)	
    cursor = connection.cursor()

    username = 'hildermes'
    firstname = 'Hildermes josé'
    middlename = 'José Medeiros Filho'
    email = 'hildermes@gmail.com'
    birthday = '1987-12-04'
    timestamp = time.strftime('%Y-%m-%d %H-%M-%S')
    password = generate_password_hash('tele')
    usertype = '2'
    
    data = []
    sql = "SELECT EXISTS(SELECT uname FROM tm_siteuser WHERE uname = %s LIMIT 1)"
    adr = ("hildermes", )
    cursor.execute(sql, adr)
#converting tuple to list    
    data = list(cursor.fetchone())
    print(str(data))
    cursor.close()
    connection.close()
    if data[0] == 0:
        print('O adm não existe, irei adicionalo')
        print('username = hildermes')
        print('password = tele')
        connection = mysql.connector.connect(**config)	
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tm_siteuser(uname,fname,mname,email,niver,t1,hashpass,typeid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(username,firstname,middlename,email,birthday,timestamp,password,usertype))
        cursor.close()
    #commit data do database
        connection.commit()
        connection.close()
    else:
        print('hildermes já foi adicionado a base')   
#    except:
#        print('hildermes já foi adicionado a base')
#    finally:
#        print('Hildermes adicionado a base')       
                
add_hildermes()
'''
testing if getting users works
userslist = gettingUsers()
print(userslist) 
username = 'hildermes'
for dic in userslist:
    if dic['username'] == username:
        print(str(dic['username']))
        hashpass = dic['password']
        print(hashpass)         
'''          
@auth.verify_password
def verify_password(username, password):
    userslist = gettingUsers()
    for dic in userslist:
        if dic['username'] == username:
            hashpass = dic['password']
            return check_password_hash(hashpass, password)
    return False
    
class signinForm(FlaskForm):
	#flask recommendation is to use inputRequired instead of datarequired
    username = StringField('Nome do usuário', validators = [DataRequired()])
    password = PasswordField('senha', validators=[InputRequired()])

@app.route('/')
@auth.login_required
def index():
    return "Seja bem vindo, %s!" % auth.username()


##Coonection to external port, binding to
if __name__ == '__main__':
    app.run(host='0.0.0.0')
