from typing import List, Dict
from flask import Flask, request, render_template, json
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'DoNoEVERshareittonoone'

class signinForm(FlaskForm):
	#flask recommendation is to use inputRequired instead of datarequired
    username = StringField('Nome do usuário', validators = [DataRequired()])
    password = password = PasswordField('password', validators=[InputRequired()])

def user_login() -> List[Dict]:
#database user, pswd, infos, and connection
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
#Selectin first table
    user= str('hildermes')
    cursor.execute('SELECT uname FROM tm_siteuser WHERE uname=%s',[user])
#Showing something
    data=cursor.fetchone()
    results = data
#closing the connection need to do something
    cursor.close()
#closing the db connection
    connection.close()
    return results

'''
@app.route('/')
def index() -> str:
    return json.dumps({'siteuser': user_login()})
'''
@app.route('/')
def index():
    form = signinForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form)

@app.route('/signin', methods=['GET','POST'])
def signin_page():
    form = signinForm


##Coonection to external port, binding to
if __name__ == '__main__':
    app.run(host='0.0.0.0')
