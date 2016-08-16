# Django MVC

Install python, pip, django
django-admin startproject proj
python manage.py startapp app
views.py
Both urls.py
settings.py for db conn string
models.py
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001 (database created in sqlite3)
python manage.py migrate , (NOT : python manage.py syncdb)