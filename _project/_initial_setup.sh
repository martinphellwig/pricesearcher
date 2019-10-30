#! /usr/bin/env bash
#
# Run from the project root
#
mkvirtualenv -p `which python3.7` pricesearcher
setvirtualenvproject
pip install -r _project/requirements.txt
django-admin startproject _server
mv _server __server
mv __server/* ./
rm -r __server
mkdir apps
touch apps/__init__.py
black .
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('dev@example.com', 'dev@example.com', 'password')" | python manage.py shell
