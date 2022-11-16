#!/usr/bin/python
import psycopg2
# from config import config

def connect(sql):
    """ Connect to the PostgreSQL database server and run an sql command and print the results"""
    conn = None
    try:
        
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect( 
                    host='localhost',
                    database='PyCoders',
                    user='postgres',
                    password='0000'        )

	    
        conn.autocommit = True
        cur = conn.cursor()
         
        
        cur.execute(sql)
        

        # return the command results :
        result = cur.fetchall()
        for r in result:
            print (r)
        
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
   connect("CREATE TABLE IF NOT EXISTS students( student_id int  PRIMARY KEY , name varchar(50))")
   connect("CREATE TABLE IF NOT EXISTS teachers( teacher_id int  PRIMARY KEY , name varchar(50))")
   connect("INSERT INTO students (student_id , name) VALUES (1, 'Henry')")
   connect("INSERT INTO students (student_id , name) VALUES (2, 'Y')")
   connect("INSERT INTO students (student_id , name) VALUES (3, 'X')")
   connect("INSERT INTO teachers (teacher_id , name) VALUES (1, 'John')")
   connect("INSERT INTO teachers (teacher_id, name) VALUES (2, 'X')")
   connect("INSERT INTO teachers (teacher_id, name) VALUES (3, 'Y')")

   connect("SELECT * FROM students")
   connect("SELECT * FROM teachers")
