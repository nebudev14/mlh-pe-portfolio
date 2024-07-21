# test_db.py

import unittest
from peewee import *
from playhouse.shortcuts import model_to_dict


from models.timeline import TimelinePost

MODELS = [TimelinePost]


# use an in-memory SQlite
test_db = SqliteDatabase(':memory:')

# Post Tests
def create_posts():
    first_post = TimelinePost.create(
        name="john doe",
        email='john@example.com',
        content='Hello world I\'m John!',
    )

    second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content='Hello world I\'m Jane!'
    )

    return (first_post, second_post)


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS) 
        test_db.close()
    
    def test_timeline_post(self):
        posts = create_posts()
        assert posts[0].id == 1

        second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content='Hello world I\'m Jane!'
        )
        assert posts[1].id == 2
    

    def test_timeline_get(self):
        # Create some timeline posts
        create_posts()

        # Get all timeline posts as dictionaries, excluding 'id' and 'created_at'
        all_timeline = [
            model_to_dict(p, exclude=[TimelinePost.id, TimelinePost.created_at])
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]

        assert all_timeline == [
            {
                "name": "Jane Doe",
                "email": "jane@example.com",
                "content": "Hello world I'm Jane!"
            },
            {
                "name": "john doe",
                "email": "john@example.com",
                "content": "Hello world I'm John!"
            }
        ]
