from typing import List, Dict
from flask import Flask, request, render_template, json, g
import mysql.connector
from flask_debugtoolbar import DebugToolbarExtension
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
from backEnd import Users

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'DoNoEVERshareittosomeone'
auth = HTTPBasicAuth()
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_PROFILER_ENABLED'] = True


     
                
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
    userslist = Users.gettingUsers()
    g.user = None
    for dic in userslist:
        if dic['username'] == username:
            hashpass = dic['password']
            if check_password_hash(hashpass, password) == True:
                return True  
    return False
    
class signinForm(FlaskForm):
	#flask recommendation is to use inputRequired instead of datarequired
    username = StringField('Nome do usuário', validators = [DataRequired()])
    password = PasswordField('senha', validators=[InputRequired()])
	
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET','POST'])
@auth.login_required
def signin():
    try:
        form = signinForm(FlaskForm)
        error = None
        if form.validate_on_submit() and verify_password(username,password) == True:
            g.user = username           
            next = flask.request.args.get('next')
            #this a MUST to prevent redirect injections
            if not is_safe_url(next):
                return flask.abort(400)
        return flask.redirect(next or flask.url_for('index'))   
    except:
        error = 'Houve algum erro ao logar'  
    return render_template('signin.html', error=error)

@app.route("/logout")
@auth.login_required
def logout():
    logout_user()
    return redirect('/')
    
##Coonection to external port, binding to
if __name__ == '__main__':
    app.run(host='0.0.0.0')
