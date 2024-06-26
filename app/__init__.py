import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

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