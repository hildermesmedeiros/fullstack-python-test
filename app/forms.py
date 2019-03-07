# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, DecimalField, TextAreaField
#for some reason 
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired, Length, Regexp
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
    #MUST change your create my on html5 field, this one won't do.
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
    username = TextField(
    'Nome', [DataRequired()]
    )
    password = PasswordField(
    'Senha', [DataRequired()]
    )

class ProductsForm(FlaskForm):
    ProductName = TextField(
    'Nome do produto', [DataRequired()]
    )
    description = TextAreaField(
    'Descrição', [DataRequired()]
    )
    price = DecimalField(
    'R$',[DataRequired()], places=2, rounding=None 
    )
    def validate_price(self, price):
        if Regexp(price.data) == False:
            raise ValidationError('Número entre RS 0 e RS 999999.99')
            
#Should implemment, add email auth first
class ForgotForm(FlaskForm):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
