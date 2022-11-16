#!/usr/bin/python
import psycopg2
from config import config

def connect(sql):
    """ Connect to the PostgreSQL database server and run an sql command and print the results"""
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		        # create a cursor
        cur = conn.cursor()
        	# execute a statement
        
        cur.execute(sql)

        # return the command results :
        result = cur.fetchall()
        for r in result:
            print (r)
        # print(result)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
   connect('select * from actor')
   connect('select * from category limit 1')
   connect('select * from address limit 50')
   
