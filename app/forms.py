# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired, Length

# Set form classes here.


class RegisterForm(FlaskForm):
    name = TextField(
        'Nome', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Senha', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repita a Senha',
        [DataRequired(),
        EqualTo('Senha', message='As senhas devem ser iguais')]
    )


class LoginForm(FlaskForm):
    name = TextField('Nome', [DataRequired()])
    password = PasswordField('Senha', [DataRequired()])


class ForgotForm(FlaskForm):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
