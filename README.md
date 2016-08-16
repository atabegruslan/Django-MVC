# Django MVC

### Steps

1. Install python, pip & django

2. Create project `django-admin startproject tripadvisor`

3. Create app `python manage.py startapp ratings`

4. Start writing the `views.py` file and both of the `urls.py` files

5. Start writing the `settings.py` file, for database connection string

6. Start writing the `models.py` file

7. `python manage.py makemigrations polls`

8. Create database in sqlite `python manage.py sqlmigrate polls 0001`

9. `python manage.py migrate`

Optional: add some initial data

```py
$python manage.py shell
>>>from ratings.models import Ratings
>>>dest1 = Ratings()
>>>dest1.destination = 'Istanbul'
>>>dest1.country = 'Turkey'
>>>dest1.rating = 'Architectural'
>>>dest1.save()
```

### Codes

#### 

```py

```

`python manage.py runserver`

### Results

![](https://raw.githubusercontent.com/atabegruslan/Django-MVC/master/Illustrations/01.PNG)
