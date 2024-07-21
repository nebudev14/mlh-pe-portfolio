import os
import re
from flask import Flask, render_template, request, abort

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
    return render_template("about.html", title="Warren Yun", routes=routes)

@app.route('/timeline')
def timeline():
    return render_template("timeline.html", title="Warren's Timeline", routes=routes)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    """ Added to Make Testing Pass - Ethan """
    required_fields = {'name', 'email', 'content'}
    provided_fields = set(request.form.keys())
    
    missing_fields = required_fields - provided_fields
    
    if missing_fields:
        abort(400, description=f"Invalid {', '.join(missing_fields)}")

    name = request.form['name']
    email = request.form['email']
    content = request.form['content']

    if not content: # checks if content is empty
        abort(400, description=f"Invalid content")
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):    # checks if email is formatted as an email
        abort(400, description=f"Invalid email")

    """ END OF FIELD CHECK - Ethan """

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

