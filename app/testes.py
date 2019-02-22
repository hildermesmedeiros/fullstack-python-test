from backEnd import Users
from backEnd import products
import time  
#import datetime

Users.gettingUsers()
#(username, firstname, middlename, email, birthday, password, usertype)
Users.add_user('hildermes','Hildermes José','Medeiros Filho', 'hildermes@gmail.com','1987-12-04', 'tele', '2')
Users.add_user('Carlos','Hernesto','Medeiros', 'carlos@gmail.com','1948-07-05', 'carlgomes', '1')
Users.gettingUsers()

#(username, product_name, product_description, product_price):
products.insert_product('hildermes', 'luvas médicas', '100 luvas de latex descartáveis', 'R$ 29,90')
products.show_product_info('1')

products.insert_product('hildermes', 'cadeiras de roda', 'cadeira de roda elétrica', 'R$ 7900,90')
products.show_product_info('2')
products.delete_product_by_id('2')
products.show_product_info('2')


products.update_product('1', 'Product Name': 'carro' , 'Product Description': 'ambulância', 'Product Price': 'R$ 100.000,00')
products.show_product_info('1')
