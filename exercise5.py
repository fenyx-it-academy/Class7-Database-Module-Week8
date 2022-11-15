import psycopg2


conn = psycopg2.connect(
            host="localhost",
            database="PyCoders",
            user="postgres",
            password="postgres")

cur = conn.cursor()

# cur.execute(
#     """
#     CREATE TABLE student (
#         student_id SERIAL PRIMARY KEY,
#         student_name VARCHAR(255) NOT NULL
#     )
#     """
#     ,
#     """ 
#     CREATE TABLE teacher (
#         teacher_id SERIAL PRIMARY KEY,
#         teacher_name VARCHAR(255) NOT NULL
#     )
#     """)

data1 = [(1, 'Saffet'), (2, 'Ahmet'), (3, 'Mehmet')]
data2 = [(1, 'John'), (2, 'Jeremy'), (3, 'Tom')]

for x in data1:
    cur.execute("INSERT INTO student (student_id, student_name) VALUES (%s,%s)", x)

for y in data2:
    cur.execute("INSERT INTO teacher (teacher_id, teacher_name) VALUES (%s,%s)", y)
    
cur.execute("SELECT * FROM student")
cur.fetchall()

cur.execute("SELECT * FROM student")
cur.fetchall()

conn.commit()
conn.close()
