from django.shortcuts import render
from django.views.generic import CreateView
from .models import blogs

# Create your views here.
def index(request):
	return render(request,'blog_menu.html')

def addblog(request):
	return render(request,'addblog.html')

class Blogs_view(CreateView):
	model=blogs
	fields=('Title','Blog','Author')
		