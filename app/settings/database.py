import re
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
      
def exec_sql_file(sql_file):
    statement = ""
    for line in open(sql_file):
        conn = connect()
        cursor = conn.cursor()
        if re.match(r'--', line):  # ignore sql comment lines
            continue
        if not re.search(r';$', line):  # keep appending lines that don't end in ';'
            statement = statement + line
        else:  # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line
            cursor.execute(statement)
            statement = ""    
            conn.commit()
            conn.close()

    
 
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