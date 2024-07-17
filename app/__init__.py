import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *

load_dotenv()
app = Flask(__name__)

routes = []
for page in os.listdir(os.getcwd() + "/app/templates"):
    if page != "index.html":
        routes.append(page.removesuffix(".html"))


@app.route('/')
def index():
    return render_template('index.html', title="Warren Yun", url=os.getenv("URL"), routes=routes)

@app.route('/about')
def about():
    return render_template("about.html", title="Warren Yun")

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
	user=os.getenv("MYSQL_USER"),
	password=os.getenv("MYSQL_PASSWORD"),
	host=os.getenv("MYSQL_HOST"),
	port=3306
)

print(mydb)
