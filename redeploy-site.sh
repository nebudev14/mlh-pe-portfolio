#!/bin/bash

cd ~/mlh-pe-portfolio
git fetch && git reset origin/main --hard
python -m pip install -r "requirements.txt"
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
