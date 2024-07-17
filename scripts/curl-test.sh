#!/bin/bash

curl --request POST http://localhost:5000/api/timeline_post -d 'name=Warren&email=hi@wyun.dev&content=I like video games.'

curl http://localhost:5000/api/timeline_post
            

