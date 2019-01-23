from django.urls import path
from . import views


urlpatterns = [
path('addblog/',views.addblog,name='addblog'),
path('addblog/save/',views.save,name='saveblog'),
path('read/',views.read,name='readblog'),
]