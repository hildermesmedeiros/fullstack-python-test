### Before using docker try
    sudo pip install virtualenv
    sudo apt-get install docker-compose
##### on linux run
    docker-compose build
##### then
    docker-compose up db
##### wait till you see it binded to the correct adress (port: 33060)
##### then
##### this will run only the test.py we are under development
    docker-compose up app
# @signin
##### check user name and password, compares to hash password and username
##### Signin extends index.html, if the user is logged and password is right. User Log's in.

# @signup




#### Docker could'nt see my images or css, I think might need nginx or some server emulation Or my CP folders are not rightly set   

##### So far, only log user in and does nothing more.
