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
# @/signin to be used with post methods
    Users.gettingUsers()
###### returns a list of dictionarys with usernames and hashpassword
###### To use when checking user name and password, compares to hash password and username

# @/signup to be used with post methods
   Users.add_user(username, firstname, middlename, email, birthday, password, usertype)
###### Adds user to database inputs:
###### auto generates timestamp, that shows user add date or last time user info got updated.

# @/products  to be used with post methods
   market.insert_product(username, product_name, product_description, product_price)
###### Adds products related to username, auto insert username id
   market.show_produtct_info(product_id)
###### shows product info, search by id
# @/products/{id} Delete
   market.delete_product_by_id(product_id)
###### deletes product by id
# @/products/{id} Update
   market.update_product(product_id, Dict)
###### Receives products id and a dictionary {'Product Name': value , 'Product Description': value', 'Product Price': value}
   market.update_product('1',{'Product Name': 'carro' , 'Product Description': 'ambulância', 'Product Price': 'R$ 100.000,00'})
# @/orders 

# @/orders/{orderId}

# @/
#### Docker could'nt see my images or css, I think might need nginx or some server emulation Or my CP folders are not rightly set   

##### So far, only log user in and does nothing more.
