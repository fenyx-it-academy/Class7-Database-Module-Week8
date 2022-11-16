import psycopg2
# from config import config


def create_tables():
	""" create tables in the PostgreSQL database"""
	commands = (
		"""
 		
		CREATE TABLE IF NOT EXISTS public.students (
			student_id SERIAL PRIMARY KEY,
			student_name VARCHAR(255) NOT NULL
		)
		""",
		""" CREATE TABLE IF NOT EXISTS public.teachers (
				teacher_id SERIAL PRIMARY KEY,
				teacher_name VARCHAR(255) NOT NULL
				)
		""")
	conn = psycopg2.connect(
	host="localhost",
	database="PyCoders",
	user="postgres",
	password="postgres")
	try:
		cur = conn.cursor()
		for command in commands:
			cur.execute(command)
   
		student_list=['sefa','saffet','ilter']		
		for i in student_list:
			postgres_insert_query = f""" INSERT INTO students (student_name) VALUES ('{i}')"""
			cur.execute(postgres_insert_query)
   			
		teacher_list=['irfan','semih','irem']
		for i in teacher_list:
			postgres_insert_query2 = f""" INSERT INTO teachers (teacher_name) VALUES ('{i}')"""
			cur.execute(postgres_insert_query2)
		cur.close()
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

if __name__ == '__main__':
	create_tables()
