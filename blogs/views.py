from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import blogs
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request,'blog_menu.html')

def addblog(request):
	return render(request,'addblog.html',{})

def save(request):
	Author=request.POST.get('author')
	Title=request.POST.get('title')
	Article=request.POST.get('article')
	print(Author)
	blog=blogs(Title=Title,Blog=Article,Author=Author)
	blog.save()
	return HttpResponseRedirect("/")

class Blogs_view(CreateView):	
	model=blogs
	fields=['Title','Blog','Author']
		