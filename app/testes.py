# -*- coding: utf-8 -*-
from backEnd import Users
from backEnd.models import tm_siteuser
from backEnd import products
import time
from backEnd import app, db  
from backEnd.models import tm_siteuser
from backEnd import bcrypt
#import datetime

Users.add_user('hildermes', 'Hildermes José', 'Medeiros', 'hildermes@gmail.com', '1987-12-04','tele', 1)
hildermes=tm_siteuser.query.filter_by(username='hildermes').first()
print(hildermes.username)
print(hildermes.hashpass)
password=bcrypt.generate_password_hash(u'hildermes').decode('utf-8')
print(password)
a=bcrypt.check_password_hash(hildermes.hashpass,'tele')
print(a)
#Users.add_user('Carlos','Hernesto','Medeiros', 'carlos@gmail.com','1948-07-05', 'carlgomes', 1)
Users.add_user('teste1','Hernesto','Medeiros', 'teste1@gmail.com','1948-07-05', 'carlgomes', 1)
'''
#(username, product_name, product_description, product_price):
products.insert_product('hildermes', 'luvas médicas', '100 luvas de latex descartáveis', 'R$ 29,90')
products.show_product_info('1')

products.insert_product('hildermes', 'cadeiras de roda', 'cadeira de roda elétrica', 'R$ 7900,90')
products.show_product_info('2')
products.delete_product_by_id('2')
products.show_product_info('2')


products.update_product('1', {'Product Name': 'carro' , 'Product Description': 'ambulância', 'Product Price': 'R$ 100.000,00'})
products.show_product_info('1')
'''
print(" ___             ___       _____   ___     ___  _____    ____")
print("|     |\\    |  |    \\        |    |       /       |     /  ")
print("|     | \\   |  |     \\       |    |       |       |     |  ")
print("|---  |  \\  |  |     |       |    |---     \\      |      \\ ")
print("|     |   \\ |  |     /       |    |        /      |      /  ")
print("|___  |    \\|  |____/        |    |___  __/       |   __/   ")
print("                                                               ")
