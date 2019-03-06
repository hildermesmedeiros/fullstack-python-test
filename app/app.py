# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import (Flask, render_template, request, flash, redirect,
    url_for, abort, g, session)
from flask_login import (current_user, login_user, login_required, logout_user, confirm_login)
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
from backEnd import Users
#importing loging instanciated in the init
from backEnd import login_manager
# Automatically tear down SQLAlchemy.




toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#
@app.route('/', methods=['GET', 'POST'], endpoint='home')
def home(): 
    if current_user.is_authenticated:
        user_id=session['user_id']
        return redirect(url_for('homewithuser', user_id=user_id))
    return render_template('pages/placeholder.home.html')

@app.route('/user/<user_id>', methods=['GET','POST'], endpoint = 'homewithuser')
def homewithuser(user_id):
    user_id=session['user_id']
    return render_template('pages/placeholder.homewithuser.html')
    
@app.route('/about', methods=['GET', 'POST'], endpoint='about')
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/user/<user_id>/about', methods=['GET', 'POST'], endpoint='aboutuser')
def about(user_id):
    user_id=session['user_id']
    return render_template('pages/placeholder.aboutuser.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == False:
        logging.warning("Signin post ")
        form = LoginForm(request.form)
        if request.method == 'POST':
            if form.validate_on_submit():
                user = tm_siteuser.query.filter_by(username=request.form['username']).first()
                logging.warning(str(user))
                if user is not None and bcrypt.check_password_hash(
                    user.hashpass, request.form['password']
                ):
                    login_user(user)
                    user_id =session['user_id']
                    return redirect(url_for('homewithuser', user_id=user_id))
                
        return render_template('forms/signin.html', form=form) 
    elif current_user.is_authenticated:
        user_id=session['user_id']
        return redirect(url_for('homewithuser', user_id=user_id))    
             
@app.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('home'))
    
@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        user = tm_siteuser.query.filter_by(username=session["user_id"]).first()
        user_id = session['user_id']
        return redirect(url_for('homewithuser', user_id=user_id))
        
    elif current_user.is_authenticated == False:  
        form = RegisterForm(request.form)
        commiterror = None
        otherError = None
        logging.warning('User must fill form send true post')
        
        if request.method == "POST" and form.validate():
            logging.warning('Form validated, trying to submit')
            Users.add_user(
                username = form.name.data,
                firstname = form.firstname.data,
                middlename = form.middlename.data,
                email = form.email.data,
                birthday = form.birthday.data,
                #models converts pass to hash
                password = form.password.data,
                usertype = 1             
            )
            
            if commiterror == None and otherError== None:
                return redirect(url_for('login'))
            else:        
                pass
        #flash(form.errors)
        #flash(form.birthday.data)
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


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0')
