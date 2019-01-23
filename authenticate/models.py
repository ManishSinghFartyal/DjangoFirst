from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=40)	
	userId = models.CharField(max_length=40)	
	dob = models.DateField()	
	password=models.TextField()