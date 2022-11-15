#!/usr/bin/python
import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:        
        # connect to the PostgreSQL server
        print('Connecting to the pagila database...')
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'pagila',
            user = 'postgres',
            password = 3678)

        # create a cursor
        cur = conn.cursor()
        
	    # execute a statement
        cur.execute('SELECT * FROM public.actor')

        # display the result
        result = cur.fetchmany(5)
        # result = cur.fetchall()
        # result = cur.fetchone()
        for r in result:
            print(r)
       
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



