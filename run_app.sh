#!/bin/bash
echo "Run django app"
source ./venv/bin/activate
cd ./Invest
python3 manage.py runserver 5000
