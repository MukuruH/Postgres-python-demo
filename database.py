import psycopg2
import psycopg2.extras

class DatabaseConnection:
	def __init__(self):
		if os.getenv('APP_SETTINGS') == 'test_db':
            self.db = 'test_db'
        else:
            self.db = 'stackoverflow'

		# connection = psycopg2.connect(dbname=self.db, user='phillip', password='password123', host='localhost', port='5432')
		connection = psycopg2.connect(dbname='dcqtq6lt2rch47', user='rzkfzvouaginmd', password='80d4f31f92593efe13bf6d5a51fc84b27d98e28478e877b16c5dadc637501205', host='ec2-54-221-207-184.compute-1.amazonaws.com', port='5432')
		connection.autocommit = True
		self.cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
		print(self.cursor)

		create_parcel_table = """CREATE TABLE IF NOT EXISTS parcel(id SERIAL PRIMARY KEY,
		name VARCHAR(100), source VARCHAR(100), destination VARCHAR(100), 
		price INT, delivered BOOLEAN, delivery_date DATE);"""
		print(create_parcel_table)
		self.cursor.execute(create_parcel_table)


	def get_all_parcel(self):
		sql_command = """
		select * from parcel;
		"""
		self.cursor.execute(sql_command)
		rows = self.cursor.fetchall()
		return rows

	def create_parcel(self, name, source, destination,price, delivery_date, delivered):
		sql_command = """
		INSERT INTO parcel (name, source, destination, price, delivery_date, delivered) 
		values ('{name}', '{source}', '{destination}', {price}, '{delivery_date}', {delivered});
		""".format(name=name, source=source, destination=destination, 
			price=price, delivery_date=delivery_date, delivered=delivered)

		self.cursor.execute(sql_command)
		rowcount = self.cursor.rowcount
		return rowcount

