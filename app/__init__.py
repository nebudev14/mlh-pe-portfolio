import os
from flask import Flask, render_template, request

from util.db import mydb
from models.timeline import *
from playhouse.shortcuts import model_to_dict

mydb.connect()
mydb.create_tables([TimelinePost])


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

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }