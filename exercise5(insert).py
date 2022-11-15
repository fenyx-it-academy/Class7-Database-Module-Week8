import psycopg2
from config import config
# from mlxtend import psycopg2

# connection establishment
conn = psycopg2.connect(
                host="localhost",
                database="PyCoders",
                user="postgres",
                password="postgres")


# Creating a cursor object
cursor = conn.cursor()

# query to create a table in the database
# sql =  (
#         """
#         CREATE TABLE IF NOT EXISTS public.students (
#             student_id SERIAL PRIMARY KEY,
#             student_name VARCHAR(255) NOT NULL
#         )
#         """,
#         """ CREATE TABLE IF NOT EXISTS public.teachers (
#                 teacher_id SERIAL PRIMARY KEY,
#                 teacher_name VARCHAR(255) NOT NULL
#                 )
#         """)
 

# # executing the query inorder to create the table
# cursor.execute(sql)
# print("Database has been created successfully !!")


  
# list to be inserted into table
data1 = [[1, 'Ahmet'],[2, 'Mehmet'], [3,'Meral']]
data2 = [[1, 'Ali'],[2, 'Rana'], [3,'Nihal']]
  
# inserting record into school table
for d1 in data1:
    # postgres_insert_query = f""" INSERT INTO student (student_id, student_name) VALUES ('{d1[0]}','{d1[1]}')"""
    # cursor.execute("""INSERT INTO student (student_id, student_name) VALUES ('{d1[0]}','{d1[1]}'""")
    cursor.execute("INSERT into student(student_id, student_name) VALUES (%s, %s)", d1)
    print("List has been inserted to student table successfully...")

for d2 in data2:
    # cursor.execute("""INSERT INTO teacher (teacher_id, teacher_name) VALUES ('{d2[0]}','{d2[1]}'""")
    cursor.execute("INSERT into teacher(teacher_id, teacher_name) VALUES (%s, %s)", d2)
    print("List has been inserted to teacher table successfully...")


# Commit your changes in the database
conn.commit()

# print("Retrieving records from table")
cursor.execute("select * from student")
records = cursor.fetchall()

for row in records:
    print("ID = ", row[0])
    print("Name = ", row[1])

cursor.execute("select * from teacher")
records = cursor.fetchall()

for row in records:
    print("ID = ", row[0])
    print("Name = ", row[1])
    
# Closing the connection
conn.close()