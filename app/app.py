# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import (Flask, render_template, request, g, session, flash, redirect,
    url_for, abort)
from functools import wraps
import logging
from logging import Formatter, FileHandler
from forms import *
import os
#----------------------------------------------------------------------------#
# Mybackends (testing)
#----------------------------------------------------------------------------#
from backEnd import app, db
#from backEnd import Users

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('Você Precisa Logar Primeiro.')
            return redirect(url_for('login'))
    return wrap

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        if form.validate_on_submit() and verify_password(username,password) == False:
            flash('Senha ou usuário inválidos. Tente Novamente.')
        else:
            g.user = username
            session['logged_in'] = True
            flash('Bem  vindo', )
            return redirect(url_for('home'))
    return render_template('forms/login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Você deslogu')
    return redirect(url_for('home'))
    
@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)


# Error handlers.
@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
