#!/bin/sh

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py createsu
gunicorn project.wsgi 
 