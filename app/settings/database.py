import mariadb
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")
PORT = int(os.getenv("PORT"))

# Connect to MySQL
def connect():
    return mariadb.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        port=PORT
    )
    
def init_db():
    basic_queries([
        ('''CREATE OR REPLACE TABLE characters (
            id int auto_increment primary key not null, 
            classe varchar(100) not null, 
            nom varchar(255) not null, 
            serveur varchar(100) not null, 
            isdeleted boolean,
            creation_date DATETIME, 
            modification_date DATETIME
            )''', 
            None),
        ('''INSERT INTO characters 
            (nom, classe, serveur, isdeleted, creation_date, modification_date) 
            VALUES ("Zoelhya", "eliotrope", "Tylezia", false, ?, ?)''', 
            (datetime.now(), datetime.now())
            ),
        ('''INSERT INTO characters 
            (nom, classe, serveur, isdeleted, creation_date, modification_date) 
            VALUES ("Cataliama", "cra", "Tylezia", false, ?, ?)''', 
            (datetime.now(), datetime.now())
        ),
        ('''INSERT INTO characters 
            (nom, classe, serveur, isdeleted, creation_date, modification_date) 
            VALUES ("Palancar", "eniripsa", "Tylezia", false, ?, ?)''', 
            (datetime.now(), datetime.now())
        )
        ])
 
def basic_query(query :str, value :tuple = None):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, value)
    conn.commit()
    conn.close()
    return cursor


def basic_queries(queries :list):
    # queries must be a list of tuple, first element the query as a string, second element the values to add in the query
    # ex : [("SELECT * FROM DTREE WHERE DATAID = ?", (2,)), ("SELECT * FROM llattrdata WHERE attrid = ?"), (12,)]
    conn = connect()
    cursor = conn.cursor()
    for query in queries:
        cursor.execute(query[0], query[1])
    conn.commit()
    conn.close()
    return cursor