import os
import psycopg2
from dotenv import load_dotenv
from database_build import build_users, build_tweets, build_entities

load_dotenv()

host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DB')
user = os.getenv('USER')
passw = os.getenv('PASS')

sql_build = [ build_users, build_tweets, build_entities ]

try:
    # Create connection to server
    db = psycopg2.connect(host=host,database=database,port=port,user=user,password=passw)

    print("Connected to database successfully.")

    # Initiate database cursor
    command_handler = db.cursor()

except Exception as e:

    print(e)
    print("Connection was unsuccessful.")

def build():

    '''Init function that creates the new database tables'''

    try:

        # Execute SQL commands
        for sql in sql_build:
            # Create tables
            command_handler.execute(sql)
        print("Table created successfully.")

    except Exception as e:

        print(e)
        print("Build unsuccessful.")

    # Close communication with server
    db.commit()
    print("Build committed.")

build()