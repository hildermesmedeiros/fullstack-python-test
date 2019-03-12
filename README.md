### Before using docker try
    sudo pip install virtualenv
    sudo apt-get install docker-compose
##### on linux run
    docker-compose build
##### then
    docker-compose up
# @/signin
![signin](/screenshots/signin.gif)


# @/signup to be used with post methods
   Users.add_user(username, firstname, middlename, email, birthday, password, usertype)
###### Adds user to database inputs:
###### auto generates timestamp, that shows user add date or last time user info got updated.

# @/products  to be used with post methods
   products.insert_product(username, product_name, product_description, product_price)
###### Adds products related to username, auto insert username id
   products.show_produtct_info(product_id)
###### shows product info, search by id
# @/products/{id} Delete
   products.delete_product_by_id(product_id)
###### deletes product by id
# @/products/{id} Update
   products.update_product(product_id, Dict)
###### Receives products id and a dictionary {'Product Name': value , 'Product Description': value', 'Product Price': value}
   products.update_product('1',{'Product Name': 'carro' , 'Product Description': 'ambulância', 'Product Price': 'R$ 100.000,00'})
# @/orders 

# @/orders/{orderId}

# @/
#### Docker could'nt see my images or css, I think might need nginx or some server emulation Or my CP folders are not rightly set   

##### So far, only log user in and does nothing more.
