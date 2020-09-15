# Django MVC

### Steps

1. Install Python, PIP & Django 

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

#### tripadvisor/tripadvisor/urls.py

```py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^ratings/', include('ratings.urls')),
]
```

#### tripadvisor/tripadvisor/settings.py

```py
INSTALLED_APPS = [
    'ratings.apps.RatingsConfig',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

#### tripadvisor/ratings/urls.py

```py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'readOne/(\w+)', views.readOne, name='readOne'),
	url(r'read', views.read, name='read'),
	url(r'create', views.create, name='create'),
	url(r'update/(\w+)', views.update, name='update'),
	url(r'delete/(\w+)', views.delete, name='delete'),
]
```

#### tripadvisor/ratings/views.py

```py
from django.shortcuts import render, redirect
from ratings.models import Ratings
from ratings.forms import NewRatingForm

def read(request):
	if request.method == "GET":
		objects = Ratings.objects.all() 
		return render(request, "ratings.html", {'res' : objects})	

def create(request):
	if request.method == "POST":
		newRatingForm = NewRatingForm(request.POST or None)
		
		if newRatingForm.is_valid():
			newRatingForm.save()

		return redirect('/ratings/read')

def update(request, dest):
	if request.method == "POST":
		t = Ratings.objects.get(destination=dest)
		t.rating = request.POST.get('rating', '')
		t.save()

		return redirect('/ratings/read')

def readOne(request, dest):
	if request.method == "GET":
		object = Ratings.objects.get(destination=dest) 
		return render(request, "ratings.html", {'res' : [ object ] })	

def delete(request, dest):
	Ratings.objects.filter(destination=dest).delete() 
	return redirect('/ratings/read')
```

#### tripadvisor/ratings/models.py

```py
from django.db import models

# Create your models here.
class Ratings(models.Model):
	destination = models.CharField(max_length = 20)
	country = models.CharField(max_length = 20)
	rating = models.CharField(max_length = 50)
```

#### tripadvisor/ratings/forms.py

```py
from django import forms
from ratings.models import Ratings

class NewRatingForm(forms.ModelForm):
 class Meta:
  model = Ratings
  fields = ['destination','country','rating']
```

#### tripadvisor/ratings/templates/template.html

```py
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha/css/bootstrap.min.css">
<style>
	h1, a{
		position:relative;
		margin:30px;
	}
</style>
{% block content %}
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha/js/bootstrap.min.js"></script>
{% endblock %}	
```

#### tripadvisor/ratings/templates/ratings.htm

```py
{% extends "template.html" %}
{% block content %}

<div class="container">
	<div class="row">
		<h1>Trip Advisor</h1>
	</div>
	<div class="row">
		<h2>
			<a href = "/ratings/read">See All</a>
		</h2>
	</div>
	<div class="row">

		<table class="table">
			<thead>
				<tr>
					<td><h3>Destination</h3></td>
					<td><h3>Country</h3></td>
					<td><h3>Rating</h3></td>
					<td></td>
				</tr>
			</thead>
			<tbody>
				{% for entry in res %}
				<tr>
					<td>
						<a href = "/ratings/readOne/{{entry.destination}}">{{entry.destination}}</a>
					</td>
					<td>{{entry.country}}</td>
					<td>
						<form class="form-inline" role="form" name = "form" action = "/ratings/update/{{entry.destination}}" method = "POST" >{% csrf_token %}
							<input class="form-control" type = "text" name = "rating" value = "{{entry.rating}}" />
							<input class="btn btn-default" type = "submit" value = "Update" />
						</form>	
					</td>
					<td>
						<a href = "/ratings/delete/{{entry.destination}}">Delete</a>
					</td>
				</tr>
				{% endfor %}	
			</tbody>
		</table>

	</div>
	<div class="row">
	
		<form class="form-inline" role="form" name = "form" action = "/ratings/create" method = "POST" >{% csrf_token %}
			<input class="form-control" type = "text" name = "destination" />
			<input class="form-control" type = "text" name = "country" />
			<input class="form-control" type = "text" name = "rating" />
			<input class="btn btn-default" type = "submit" value = "Create" />
		</form>

	</div>	
</div>

{% endblock %}	
```

`python manage.py runserver`

### Results

![](https://raw.githubusercontent.com/atabegruslan/Django-MVC/master/Illustrations/01.PNG)

---

## Tutorials

- Python
    - https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3
    - https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
- Django
    - https://www.youtube.com/playlist?list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau
    - https://www.youtube.com/watch?v=VuETrwKYLTM&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=87
