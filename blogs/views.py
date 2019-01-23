from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import blogs
from django.http import HttpResponse,HttpResponseRedirect


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


def read(request):
	all_blogs=blogs.objects.all()
	for blog in all_blogs:
		print(blog.Title)
		print(blog.Author)
		print(blog.Blog)
	return render(request,"readblogs.html",{'Blogs':all_blogs})


class Blogs_view(CreateView):	
	model=blogs
	fields=['Title','Blog','Author']
		