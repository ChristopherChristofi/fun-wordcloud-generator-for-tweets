import os
import psycopg2
from dotenv import load_dotenv
from database_build import build_commands

load_dotenv()

host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DB')
user = os.getenv('USER')
passw = os.getenv('PASS')

def main():
    '''Init function that creates the new database tables'''

    try:
        # Create connection to server
        db = psycopg2.connect(host=host,database=database,port=port,user=user,password=passw)

        print("Connected to database successfully.")

        # Initiate database cursor
        command_handler = db.cursor()

        # Execute SQL commands
        for command in build_commands:
            # Create tables
            command_handler.execute(command)
            print("Table created successfully.")

    except Exception as e:
        print(e)
        return print("Conection was unsuccessful.")

    # Close communication with server
    db.commit()
    command_handler.close()
    db.close()

    print("Database closed.")

main()