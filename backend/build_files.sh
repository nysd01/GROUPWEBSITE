#!/bin/bash
python3.9 -m venv venv
source venv/bin/activate
pip install --no-cache-dir -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput
