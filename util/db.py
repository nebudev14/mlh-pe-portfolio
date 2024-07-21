from dotenv import load_dotenv
from peewee import MySQLDatabase, SqliteDatabase

import os

load_dotenv()


if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
	user=os.getenv("MYSQL_USER"),
	password=os.getenv("MYSQL_PASSWORD"),
	host=os.getenv("MYSQL_HOST"),
	port=3306
)
