from typing import List, Dict
import mysql.connector
import time


def insert_product(username, product_name, product_description, product_price):    
    try:
        print("Inserindo produto")
        uname = str.lower(username)
        pname = product_name
        pdescription = product_description
        pprice = product_price
            
        config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'telemedicina'
        }
        
        connection = mysql.connector.connect(**config)	
        cursor = connection.cursor()
    
        query = []
        sql = "SELECT uname FROM tm_siteuser WHERE uname = %s LIMIT 1"
        adr = (uname, )
        cursor.execute(sql, adr)
#converting tuple to list    
        query = list(cursor.fetchone())
        cursor.close()
        connection.close()
        if query[0] == username:
            print('O usuário ',uname, 'foi encontrado produto será adicionado')
            # User type
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            sql = "SELECT typeid FROM tm_siteuser WHERE uname = %s"
            adr = (username,)
            cursor.execute(sql,adr)
            data = list(cursor.fetchone())
            userid = data[0]
            cursor.close()
            
            #first add requires first time stamp
            pcreation = time.strftime('%Y-%m-%d %H-%M-%S')
            cursor = connection.cursor()
            sql = "INSERT INTO tm_products(name,description,price,t1,user_id) VALUES(%s,%s,%s,%s,%s)"
            adr = (pname, pdescription, pprice, pcreation, userid,)
            cursor.execute(sql, adr)
            cursor.close()
            #commit data do database
            connection.commit()
            connection.close()
    except Exception as e:
        print('2 ALGUM ERRO ACONTECEU com market. Erro: ', e)
    finally:
        print('fechando')

def delete_product_by_id(product_id):
    try:
        print("deletando produto")
        config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'telemedicina'
        }
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        sql = "DELETE FROM tm_products WHERE id = %s"
        adr = (product_id,)
        cursor.execute(sql, adr)
        connection.commit()
        connection.close()
    except Exception as e:
        print("Error ",e, " ao deletar o produto de id:[",product_id,"]")
    
def show_produtct_info(product_id):
    try:
        print("Informações sobre o produto")
        config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'telemedicina'
        }
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        sql = "SELECT * FROM tm_products WHERE id = %s"
        adr = (product_id,)
        cursor.execute(sql, adr)
        data = list(cursor.fetchall())
        cursor.close()
        connection.close()
        if data[0] == 0:
            print("Produto não econtrado")
        else:    
            print(data)
    except Exception as e:
        print("Error", e, " ao buscar pelo produto de id:[", product_id,"]")
