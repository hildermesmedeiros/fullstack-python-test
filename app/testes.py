from backEnd import Users
from backEnd import market
import time  
#import datetime

Users.gettingUsers()
#(username, firstname, middlename, email, birthday, password, usertype)
Users.add_user('hildermes','Hildermes José','Medeiros Filho', 'hildermes@gmail.com','1987-12-04', 'tele', '2')
Users.add_user('Carlos','Hernesto','Medeiros', 'carlos@gmail.com','1948-07-05', 'carlgomes', '1')
Users.gettingUsers()

#(username, product_name, product_description, product_price):
market.insert_product('hildermes', 'luvas médicas', '100 luvas de latex descartáveis', 'R$ 29,90')
