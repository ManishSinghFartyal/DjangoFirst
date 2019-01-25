from django.db import models
from django.utils import timezone

# Create your models here.
class blogs(models.Model):
	Userid=models.CharField(max_length=200)
	Title = models.CharField(max_length=200)
	Blog = models.TextField()
	Author = models.CharField(max_length=200)
	Created_date =models.DateTimeField(default=timezone.now)
	Image=models.ImageField(upload_to='static/blog_image',default='NoImage.png')
