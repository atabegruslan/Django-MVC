from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'readOne/(\w+)', views.readOne, name='readOne'),
	url(r'read', views.read, name='read'),
	url(r'create', views.create, name='create'),
	url(r'update/(\w+)', views.update, name='update'),
	url(r'delete/(\w+)', views.delete, name='delete'),
]
