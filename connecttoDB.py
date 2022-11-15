#!/usr/bin/python
import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config("database.ini","learn_pagila")
        #params= {'host': 'localhost', 'database': 'Chinook_PostgreSql', 'user': 'postgres', 'password': 'postgres'}
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        conn.autocommit = True
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        # file = open('sqlcommands.sql', 'r')
        # sqlFile = file.read()
        # file.close()
        # sqlCommands = sqlFile.split(';')[:-1]
        # for command in sqlCommands:
        #     try:
        #         cur.execute(command)
        #         print(cur.fetchall())
        #     except (Exception, psycopg2.DatabaseError) as error:
        #         print("Command skipped: ", error)
        #         break


        cur.execute('SELECT * from actor;')
        print(cur.fetchall())
        cur.execute('SELECT * FROM category;')
        print(cur.fetchone())
        cur.execute('SELECT * from address;')
        print(cur.fetchmany(50))



	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()