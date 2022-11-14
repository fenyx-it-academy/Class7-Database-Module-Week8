import psycopg2
from time import sleep


def connect():
    connection = None
    sleep(0.5)
    try:
        print('Connect to the PostgreSQL database server...')
        
        connection = psycopg2.connect (
            database='pagila-data', 
            user="postgres", 
            password="Anahi0615.")
        
        connection.autocommit = True


        #  All rows from actor table fetchall
        print("+-------------------------------+")
        print("|   All rows from actor table   |")
        print("+-------------------------------+")
        cursor = connection.cursor()
        query = """ SELECT * FROM actor """
        cursor.execute(query)
        result = cursor.fetchall()
        
        for r in result:
            print(r)
            sleep(0.069)

        #  First row of category table with fetchone
        print()
        print("+-------------------------------+")
        print("|  First row of category table  |")
        print("+-------------------------------+")
        cursor = connection.cursor()
        query = """ SELECT * FROM category """
        cursor.execute(query)
        result = cursor.fetchone()
        print(result,"\n")
        sleep(0.3)


        #  50 rows of address table  fetchmany
        print("+-------------------------------+")
        print("|   50 rows of address table    |")
        print("+-------------------------------+")
        cursor = connection.cursor()
        query = """ SELECT * FROM address """
        cursor.execute(query)
        result = cursor.fetchmany(size=50)

        for r in result:
            print(r)
            sleep(0.069)

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            sleep(0.3)
            print('\nDatabase connection closed.\n')

if __name__ == '__main__':
    connect()