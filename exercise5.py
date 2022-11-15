import psycopg2
# from config import config

def connect():
    """connect to the PostgreSQL database server"""
    conn = None
    try:
        #connect to the PostgreSQL server
        print('Connecting to the PyCoders database...')
        
        conn = psycopg2.connect(
                host = "localhost",
                database = "PyCoders",
                user = "postgres",
                password = 3678)
            
        conn.autocommit = True

        #create table for students
        cur = conn.cursor()
        file = open('PyCoders.sql', 'r')
        sql = file.read()
        file.close()
        commands = sql.split(';')[:-1]
        for cmd in commands:
            try:
                cur.execute(cmd)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        select_query = 'SELECT * FROM students'
        cur.execute(select_query)
        result = cur.fetchmany(5)
        # result = cur.fetchall()
        # result = cur.fetchone()
        print(result)


        select_query2 = 'SELECT * FROM teachers'
        cur.execute(select_query2)
        result = cur.fetchmany(5)
        # result = cur.fetchall()
        # result = cur.fetchone()
        print(result)

        
        # #close the communicaton with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()


