from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def user_info() -> List[Dict]:
#database user, pswd, infos, and connection
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
#Selectin first table
    cursor.execute('SELECT * FROM siteuser')
#Showing something
    results = [{uname: email} for (uname, email) in cursor]
#closing the connection need to do something
    cursor.close()
#closing the db connection
    connection.close()
    return results


@app.route('/')
def index() -> str:
    return json.dumps({'siteuser': user_info()})

##Coonection to external port, binding to
if __name__ == '__main__':
    app.run(host='0.0.0.0')
