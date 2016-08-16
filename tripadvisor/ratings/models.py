from django.db import models

# Create your models here.
class Ratings(models.Model):
	destination = models.CharField(max_length = 20)
	country = models.CharField(max_length = 20)
	rating = models.CharField(max_length = 50)