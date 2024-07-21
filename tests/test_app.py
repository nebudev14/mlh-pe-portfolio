# tests/test_app.py
import os
os.environ['TESTING'] = 'true'

import unittest
from app import app



class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200

        html = response.get_data(as_text=True)
        assert "<title>Warren Yun</title>" in html
        assert '<img src="./static/img/warren_working.png" />' in html
        assert '<h1>Warren Yun</h1>' in html
        assert "<li>Sciborgs Robotics, Team Captain</li>" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json

        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0


        # Testing /api/timeline_post POST request
        response = self.client.post("/api/timeline_post", 
                                    data={
                                        "name": "John Doe",
                                        "email": "john@example.com",
                                        "content": "HI THERE"
                                    })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        
        json = response.get_json()
        self.assertIn("John Doe", json["name"])
        self.assertIn("john@example.com", json["email"])
        self.assertIn("HI THERE", json["content"])


        # Testing /api/timeline_post GET request
        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)

        json = response.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 1)
        self.assertEqual(json["timeline_posts"][0]["name"], "John Doe")
        self.assertEqual(json["timeline_posts"][0]["email"], "john@example.com")
        self.assertEqual(json["timeline_posts"][0]["content"], "HI THERE")


    def test_malformed_timeline(self):
        # POST request w/ missing name
        response = self.client.post("/api/timeline_post",
                        data={
                            "email": "john@example.com",
                            "content": "Hello world, I'm John!"
                            })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request w/ empty content
        response = self.client.post("/api/timeline_post", 
                        data={
                            "name": "John Doe",
                            "email": "john@example.com",
                            "content": ""
                        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html


        # POST request with malformed email
        response = self.client.post("/api/timeline_post",
                    data = {
                        "name": "John Doe",
                        "email": "johom",
                        "content": "Hello world, I'm John!"
                    })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

