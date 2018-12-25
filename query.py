import mysql.connector as mc
from mysql.connector import errorcode

def getDatabaseConnection():
	print("Trying to connect to the database...")
	try:
		connection = mc.connect (
			user = 'root',
			password = 'root',
			host = 'localhost',
			database = 'moviesdb'
		)
		print("Database connected!")
	except mc.Error as e:
		if (e.errno == errorcode.ER_ACCESS_DENIED_ERROR):
			print("Wrong user and/or password")
		elif (e.errno == errorcode.ER_BAD_DB_ERROR):
			print("Database doesn't exist")
		else:
			print(e)
	return connection

if __name__ == '__main__':
	connection = getDatabaseConnection()
	cursor = connection.cursor()

	year = input('List all movies for the year: ');
	
	for line in open('sql/movies.sql'):
		cursor.execute(line.replace('{year}', year))

	for row in cursor:
		print(row[0].split('(' + year + ')')[0])

	connection.commit()

	cursor.close()
	connection.close()