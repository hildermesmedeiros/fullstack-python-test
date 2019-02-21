from typing import List, Dict
import mysql.connector
import time
from werkzeug.security import generate_password_hash, check_password_hash  
#import datetime


#to be used in signin
def gettingUsers() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'telemedicina'
    }
    connection = mysql.connector.connect(**config)
#python postgresql connection
    cursor = connection.cursor()
#Selecting all users
    cursor.execute('SELECT uname,hashpass FROM tm_siteuser')
#fetchin data  all data from user   
#    data=cursor.fetchone()
    users = []
    for row in cursor:
        a = list(row)
        dic = {'username': a[0], 'password': a[1]}
        users.append(dic)
#closing the table connection
    cursor.close()
#closing the db connection
    connection.close()
    print(users)
    return users
    
#To be used in signup    
def add_user(username, firstname, middlename, email, birthday, password, usertype):
    try:
        config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'telemedicina'
        }
        
        connection = mysql.connector.connect(**config)	
        cursor = connection.cursor()
        
        uname =  str.lower(username)
        fname = firstname
        mname = middlename
        email = email
        niver = birthday
        #first add requires first time stamp
        timestamp = time.strftime('%Y-%m-%d %H-%M-%S')
        hashpass = generate_password_hash(password)
        typeid = usertype 
        query = []
        sql = "SELECT EXISTS(SELECT uname FROM tm_siteuser WHERE uname = %s LIMIT 1)"
        adr = (uname, )
        cursor.execute(sql, adr)
#converting tuple to list    
        query = list(cursor.fetchone())
        print(str(query))
        cursor.close()
        connection.close()
        if query[0] == 0:
            print('O usuário ',uname, 'não existe, checarei o email')
            connection = mysql.connector.connect(**config)
            query = []
            cursor = connection.cursor()
            sql = "SELECT EXISTS(SELECT email FROM tm_siteuser WHERE email = %s LIMIT 1)"
            adr = (email, )
            cursor.execute(sql, adr)
            query = list(cursor.fetchone())
            cursor.close()
            connection.close()
            if query[0] == 0:
                print('Usuário ',uname,' será adicionado')
                print('username = ', uname)
                print('password = ', password, ' we wont store it in the data base.')
                connection = mysql.connector.connect(**config)	
                cursor = connection.cursor()
                cursor.execute("INSERT INTO tm_siteuser(uname,fname,mname,email,niver,t1,hashpass,typeid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(uname,fname,mname,email,niver,timestamp,hashpass,typeid))
                cursor.close()
                #commit data do database
                connection.commit()
                connection.close()
            else:
                print(email,' já está vinculado a outro usuário')
        else:
            print(uname, 'já existe na base')   
    except Exception as e:
        print('ALGUM ERRO ACONTECEU. Erro: ', e)
    finally:
        print('fechando')
          
