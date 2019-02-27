from backEnd import Users
from backEnd.models import tm_siteuser
from backEnd import products
import time
from backEnd import app, db  
#import datetime

from werkzeug.security import generate_password_hash, check_password_hash


User = tm_siteuser(
    username = 'hildermes',
    firstname = 'Hildermes José',
    middlename = 'Medeiros',
    email = 'hildermes@gmail.com',
    birthday = '1987-12-04',
    t1 = time.strftime('%Y-%m-%d %H-%M-%S'),
    hashpass = generate_password_hash('tele'),
    typeid = 2
)
db.session.add(User)
try:
    db.session.commit()
except:
    db.session.rollback()    
username='hildermes'
userslist = tm_siteuser.query.filter_by(username=username).first()
print('users:', userslist.username)
'''
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


products.update_product('1', {'Product Name': 'carro' , 'Product Description': 'ambulância', 'Product Price': 'R$ 100.000,00'})
products.show_product_info('1')
'''
