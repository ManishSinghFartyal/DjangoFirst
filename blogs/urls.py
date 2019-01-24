from django.urls import path
from . import views


urlpatterns = [
path('',views.index,name=''),
path('addblog/',views.addblog,name='addblog'),
path('addblog/save/',views.save,name='saveblog'),
path('read/',views.read,name='readblog'),
path('read_my/<category>',views.read_my,name='readmyblog'),
]