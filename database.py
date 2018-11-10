import psycopg2
import psycopg2.extras

class DatabaseConnection:
	def __init__(self):
		if os.getenv('APP_SETTINGS') == 'test_db':
            self.db = 'test_db'
        else:
            self.db = 'stackoverflow'

		db_credentials = """
		dbname='phillip' user='phillip' password='password123'
	    host='localhost' port='5432'
		"""
		connection = psycopg2.connect(dbname=self.db, user='phillip', password='password123', host='localhost', port='5432')
		connection.autocommit = True
		self.cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
		print(self.cursor)


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

