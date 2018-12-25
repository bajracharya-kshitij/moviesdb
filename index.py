import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import os

def createTable(filename):
	data = pd.read_csv('csv/' + filename)
	engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/moviesdb', echo=False)
	data.to_sql(name=os.path.splitext(filename)[0], con=engine, if_exists = 'append', index=False)

if __name__ == '__main__':
	[createTable(filename) for filename in os.listdir('csv/') if filename.endswith('csv')]
	