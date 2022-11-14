import psycopg2
import time 
from time import sleep


def connect():
    connection = None
    sleep(0.8)
    try:
        print('Connect to the PostgreSQL database server...')
        
        connection = psycopg2.connect (
            database='PyCoders', 
            user="postgres", 
            password="Anahi0615.")
        
        connection.autocommit = True
        
        # CREATE TABLE Students
        
        cursor = connection.cursor()
        query = """ CREATE TABLE Students (
                    student_ID INT NOT NULL, 
                    student_name VARCHAR(120), 
                    CONSTRAINT PK_Students PRIMARY KEY  (student_ID)) """

        cursor.execute(query)
        

        # CREATE TABLE Teachers

        # cursor = connection.cursor()
        query = """ CREATE TABLE Teachers (
                    teacher_ID INT NOT NULL,
                    teacher_name VARCHAR(120),
                    CONSTRAINT PK_Teachers PRIMARY KEY  (teacher_ID)) """
        cursor.execute(query)
        
        # insert tData INTO Students
        
        query = """ INSERT INTO Students 
                (student_ID, student_name) 
        VALUES 
        (
            1, 'Shatha Al-Ashwal'
        ),
        (   2, 'Ghassan Alabsi'
        ), 
        (   3, 'Juan Obregon'
        ) """
        
        cursor.execute(query)

        # insert Data INTO Teachers
        query = """ INSERT INTO Teachers 
                (teacher_ID, teacher_name) 
        VALUES 
        (
            1, 'Irfan Karadeniz'
        ),
        (   2, 'Semith'
        ), 
        (   3, 'Irem Ugurlu'
        ) """
        
        cursor.execute(query)

        # viewData Student
        query = 'Select student_ID, student_name from students'
        cursor.execute(query)
        sleep(0.8)
        print('Students List :')
        for fila in cursor:
            print(fila)
            sleep(0.4)
        print()


        # viewData Teachers
        query = 'Select teacher_ID, teacher_name from Teachers'
        cursor.execute(query)
        sleep(0.8)
        print('Teachers List :')
        for fila in cursor:
            print(fila)
            sleep(0.4)
        print()

        cursor.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            sleep(0.8)
            print('Database connection closed.')

if __name__ == '__main__':
    connect()