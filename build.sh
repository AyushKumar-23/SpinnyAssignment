#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py collectstatic
python manage.py migrate

python manage.py createsuperuser
admin
admin@gmail.com
password123
password123