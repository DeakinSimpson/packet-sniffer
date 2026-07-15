import sqlite3
from pathlib import Path
import os

# checks if the data folder exists, if it doesnt create it
if not os.path.exists('data'):
    os.makedirs('data')


def db_init():
    try:
        # initialise db connection
        sqliteConnection = sqlite3.connect('data/packets.db')
        print('db init')

        # inialise curser
        curser = sqliteConnection.cursor()

    except sqlite3.Error as error:
        print('Error occured - ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection Closed')


    return sqliteConnection