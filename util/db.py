from dotenv import load_dotenv
from peewee import MySQLDatabase
import os

load_dotenv()

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
	user=os.getenv("MYSQL_USER"),
	password=os.getenv("MYSQL_PASSWORD"),
	host=os.getenv("MYSQL_HOST"),
	port=3306
)
