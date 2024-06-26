import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Warren Yun", url=os.getenv("URL"), about=os.getenv("ABOUT"))

@app.route('/about')
def about():
    return render_template("more.html", title="Warren Yun", url=os.getenv("ABOUT"))