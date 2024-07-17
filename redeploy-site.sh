#!/bin/bash

cd ~/mlh-pe-portfolio
git fetch && git reset origin/main --hard
python -m pip install -r "requirements.txt"
source ./venv/bin/activate
systemctl daemon-reload
systemctl restart myportfolio