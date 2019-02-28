# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import (Flask, render_template, request, flash, redirect,
    url_for, abort)
from flask_login import (current_user, login_user, login_required, logout_user)
from forms import *
import os
from flask_login import AnonymousUserMixin as notUser
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.urls import url_parse
import logging
#from werkzeug.security import generate_password_hash, check_password_hash
#----------------------------------------------------------------------------#
# My backends (testing)
#----------------------------------------------------------------------------#
#importing app and database (defined in init, this can cause 
#circular imports)
from backEnd import app, db
#I instanciated bycrypt in the init
from backEnd import bcrypt 
#Importing the database models
from backEnd.models import tm_siteuser
#importing loging instanciated in the init
from backEnd import login_manager
# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/', methods=['GET', 'POST'], endpoint='home')
def home():
    #If its anonymous user
    if notUser.is_anonymous:
        flash(u"Não esqueça de logar")
    elif notUser.is_anonymous==True:
        login_manager.login_message = u"Bem vindo, você acaba de logar."
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    logging.warning("See this message in Flask Debug Toolbar!")
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = tm_siteuser.query.filter_by(username=request.form['username']).first()
            logging.warning(str(user))
            if user is not None and bcrypt.check_password_hash(
                user.hashpass, request.form['password']
            ):
                login_user(user)
                flash(u'You were logged in. Go Crazy.')
                return redirect(url_for('home'))
               
    return render_template('forms/signin.html', form=form) 
                     
'''
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        if (form.validate_on_submit() and verify_password(username,password)) == False:
            flash('Senha ou usuário inválidos. Tente Novamente.')
        else:
            g.user = username
            session['logged_in'] = True
            flash('Bem  vindo', )
            return redirect(url_for('home'))
    return render_template('forms/login.html', form=form)
'''
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
    
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = tm_siteuser(
                username = form.username.data,
                email = form.email.data,
                firstname = form.firstname.data,
                middlename = form.middlename.data,
                birthday = form.birthday.data,
                #models converts pass to hash
                hashpass = form.password.data,
                timestamp = time.strftime('%Y-%m-%d %H-%M-%S'),
                typeid = 1
            )
            db.session.add(tm_siteuser)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

'''
# Error handlers.
@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404
'''

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0')
