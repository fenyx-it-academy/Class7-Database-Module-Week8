import psycopg2
# from config import config


def create_tables():
	""" create tables in the PostgreSQL database"""
	# commands = (
	# 	"""
	# 	CREATE TABLE students (
	# 		student_id SERIAL PRIMARY KEY,
	# 		student_name VARCHAR(255) NOT NULL
	# 	)
	# 	""",
	# 	""" CREATE TABLE teachers (
	# 			teacher_id SERIAL PRIMARY KEY,
	# 			teacher_name VARCHAR(255) NOT NULL
	# 			)
	# 	""")
	conn = psycopg2.connect(
	host="localhost",
	database="PyCoders",
	user="postgres",
	password="postgres")
	try:
		cur = conn.cursor()
		# for command in commands:
		# 	cur.execute(command)
		postgres_insert_query = """ INSERT INTO students (student_id, student_name) VALUES (%s,%s)"""
		postgres_insert_query2 = """ INSERT INTO teachers (teacher_id, teacher_name) VALUES (%s,%s)"""
		student_list=['sefa','saffet','ilter']
		a=1
		for i in student_list:
			record_to_insert = (a, i)
			cur.execute(postgres_insert_query, record_to_insert)
			a+=1
		teacher_list=['irfan','semih','irem']
		a=1
		for i in teacher_list:
			record_to_insert = (a, i)
			cur.execute(postgres_insert_query2, record_to_insert)
			a+=1
		cur.close()
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


if __name__ == '__main__':
	create_tables()
