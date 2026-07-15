import sqlite3
from pathlib import Path
import os

# checks if the data folder exists, if it doesnt create it
if not os.path.exists('data'):
    os.makedirs('data')

# creates the initial db
def db_init():
    try:
        # initialise db connection
        sqliteConnection = sqlite3.connect('data/packets.db')
        print('db init')

        # inialise curser
        curser = sqliteConnection.cursor()

        # create table if one doesnt already exits
        create_table_query = """
            CREATE TABLE IF NOT EXISTS PACKETS (
                id integer PRIMARY KEY AUTOINCREMENT,
                time REAL,
                src TEXT,
                dst TEXT,
                proto INTEGER,
                sport INTEGER,
                dport INTEGER,
                size INTEGER,
                dns_query TEXT,
                raw TEXT
            );
        """
        curser.execute(create_table_query)

    except sqlite3.Error as error:
        print('Error occured - ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection Closed')


    return sqliteConnection