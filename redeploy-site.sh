#!/bin/bash

cd ~/mlh-pe-portfolio
git fetch && git reset origin/main --hard
python -m pip install -r "requirements.txt"
source ./venv/bin/activate
tmux new-session -d 'flask run --host=0.0.0.0'
