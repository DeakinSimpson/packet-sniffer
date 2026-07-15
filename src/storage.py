import sqlite3
from pathlib import Path
import os

# creates the initial db
def db_init():
    # checks if the data folder exists, if it doesnt create it
    if not os.path.exists('data'):
        os.makedirs('data')

    try:
        # initialise db connection
        sqliteConnection = sqlite3.connect('data/packets.db')
        print('db init')

        # inialise curser
        curser = sqliteConnection.cursor()

        # create table if one doesnt already exits
        create_table_query = """
            CREATE TABLE IF NOT EXISTS packets (
                id integer PRIMARY KEY AUTOINCREMENT,
                time REAL,
                src TEXT,
                dst TEXT,
                proto INTEGER,
                ttl INTEGER,
                sport INTEGER,
                dport INTEGER,
                size INTEGER,
                dns_query TEXT,
                raw TEXT
            );
        """
        curser.execute(create_table_query)

    except sqlite3.Error as error:
        print('Error occured -', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection Closed')


def insertPacketDetails(packets):
    try:
        # connect to db
        sqliteConnection = sqlite3.connect('data/packets.db')
        curser = sqliteConnection.cursor()

        # insert each packet into the db
        for pkt in packets:
            curser.execute("""
                INSERT INTO packets (time, src, dst, proto, ttl, sport, dport, size, dns_query, raw) 
                VALUES (:time, :src, :dst, :proto, :ttl, :sport, :dport, :size, :dns_query, :raw)   
            """, pkt)

        sqliteConnection.commit()

    except sqlite3.Error as error:
        print('Error occured -', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection Closed')

def resetDatabase():
    try:
        # connect to db
        sqliteConnection = sqlite3.connect('data/packets.db')
        curser = sqliteConnection.cursor()

        curser.execute("DROP TABLE IF EXISTS packets")

        sqliteConnection.commit()
    
    except sqlite3.Error as error:
        print('Error occured -', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection Closed')

    db_init()
