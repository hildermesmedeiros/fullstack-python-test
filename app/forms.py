# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
#for some reason 
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired, Length
from backEnd import tm_siteuser
# Set form classes here.


class RegisterForm(FlaskForm):
    name = TextField(
        'Nome', validators=[DataRequired(), Length(min=6, max=25)]
    )
    firstname = TextField(
        'Primeiro Nome', validators=[DataRequired(), Length(min=6, max=40)]
    )
    middlename = TextField(
        'Sobre nome', validators=[DataRequired(), Length(min=6, max=40)]
    )
    birthday = DateField(
        'Data de Nascimento',format="%Y-%m-%d", validators=[DataRequired()]
    )        
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Senha', validators=[DataRequired(), Length(min=6, max=40), EqualTo('confirm', message='As senhas devem ser iguais')]
    )
    confirm = PasswordField(
        'Repita a Senha'
    )
    
    def validate_name(self, name):
        name = tm_siteuser.query.filter_by(username=name.data).first()
        if name != None:
            raise ValidationError('Este nome de usuário não está disponível')

    def validate_email(self, email):
        email = tm_siteuser.query.filter_by(email=email.data).first()
        if email != None:
            raise ValidationError('Este email já está cadastrado')

class LoginForm(FlaskForm):
    username = TextField('Nome', [DataRequired()])
    password = PasswordField('Senha', [DataRequired()])


class ForgotForm(FlaskForm):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
