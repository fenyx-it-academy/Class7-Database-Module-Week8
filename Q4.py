import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="W1_Q3_Pagila",
    user="postgres",
    password="aiham")

cur = conn.cursor()
cur.execute('select * from "actor";')
data = cur.fetchall()
print(data)

print("-----------------------------------------------------------------------------------------------------------------")

cur = conn.cursor()
cur.execute('select * from "category";')
data = cur.fetchone()
print(data)

print("-----------------------------------------------------------------------------------------------------------------")

cur = conn.cursor()
cur.execute('select * from "address";')
data = cur.fetchmany(50)
print(data)