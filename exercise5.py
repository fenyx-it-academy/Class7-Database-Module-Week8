import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="PyCoders",
        user="postgres",
        password="aiham")
cur = conn.cursor()
    
cur.execute('CREATE TABLE IF NOT EXISTS public.students(student_id integer NOT NULL,name text );')
cur.execute('CREATE TABLE IF NOT EXISTS public."teachers"(teacher_id integer NOT NULL,name text );')

insert_q = """ INSERT INTO public.students (student_id, name) VALUES (%s,%s)"""
insert_v = (1, 'Ali')
cur.execute(insert_q,insert_v)

insert_q = """ INSERT INTO public.students (student_id, name) VALUES (%s,%s)"""
insert_v = (2, 'Adham')
cur.execute(insert_q,insert_v)

insert_q = """ INSERT INTO public.students (student_id, name) VALUES (%s,%s)"""
insert_v = (3, 'Amal')
cur.execute(insert_q,insert_v)


insert_q = """ INSERT INTO public.teachers (teacher_id, name) VALUES (%s,%s)"""
insert_v = (1, 'Shatha')
cur.execute(insert_q,insert_v)

insert_q = """ INSERT INTO public.teachers (teacher_id, name) VALUES (%s,%s)"""
insert_v = (2, 'Farah')
cur.execute(insert_q,insert_v)

insert_q = """ INSERT INTO public.teachers (teacher_id, name) VALUES (%s,%s)"""
insert_v = (3, 'Sam')
cur.execute(insert_q,insert_v)

cur.execute('select * from "students";')
data = cur.fetchall()
print(data)

cur.execute('select * from "teachers";')
data = cur.fetchall()
print(data)

cur.close()
conn.commit()
conn.close()


