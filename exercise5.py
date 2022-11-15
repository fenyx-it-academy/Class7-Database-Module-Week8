#!/usr/bin/python
import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config("database.ini", "PyCoders")
        # connect to the PostgreSQL server
        print('Connecting to the PyCoders  database...')
        conn = psycopg2.connect(**params)
        conn.autocommit = True
        # create a cursor
        cur = conn.cursor()
 
        file = open('ex5sqlcommands.sql', 'r')
        sqlFile = file.read()
        file.close()
        sqlCommands = sqlFile.split(';')[:-1]
        for command in sqlCommands:
            try:
                cur.execute(command)
                # print(cur.fetchall())
            except (Exception, psycopg2.DatabaseError) as error:
                print("Command skipped because of the error: ", error)
                break


        sql_select_query='SELECT * FROM students'
        cur.execute(sql_select_query)
        print(cur.fetchall())

        sql_select_query='SELECT * FROM teachers'
        cur.execute(sql_select_query)
        print(cur.fetchall())
        cur.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()