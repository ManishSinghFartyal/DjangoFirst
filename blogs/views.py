from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import blogs
from django.http import HttpResponse,HttpResponseRedirect
from .service.Googlesearch import fetch_result
from .service.MostOccured import list_of_most_occured

def index(request):
	return render(request,'blog_menu.html',{})
	
def addblog(request):
	return render(request,'addblog.html',{})


def save(request):
	Author=request.POST.get('author')
	Title=request.POST.get('title')
	Article=request.POST.get('article')
	#print(Author)		
	blog=blogs(Title=Title,Blog=Article,Author=Author)
	blog.save()
	return HttpResponseRedirect("/")


def read(request):
	new_dics={}
	all_blogs=blogs.objects.all()
	for blog in all_blogs:								
		str1=list_of_most_occured(blog.Blog)	
		res=fetch_result(str1,4)
		#print(str1,"\n related links")
		new_dics[blog.id]={'title':blog.Title,'Blog':blog.Blog,'Author':blog.Author,'Date':blog.Created_date,'Links':res}					
		'''
		for key,value in res.items():
			if key =="":
				continue
			try:
				new_dics[blog.id][key]=value
			except:
				continue
		'''
	print(new_dics)	
	return render(request,"readblogs.html",{'Blogs':new_dics})


class Blogs_view(CreateView):	
	model=blogs
	fields=['Title','Blog','Author']
		