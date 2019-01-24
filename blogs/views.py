from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import blogs
from django.http import HttpResponse,HttpResponseRedirect
from .service.Googlesearch import fetch_result
from .service.MostOccured import list_of_most_occured
from django.contrib import messages

def index(request):
	return render(request,'blog_menu.html',{})
	
def addblog(request):
	return render(request,'addblog.html',{})


def save(request):
	Author=request.POST.get('author')
	Title=request.POST.get('title')
	Article=request.POST.get('article')
	Userid=request.session['userid']
	#print(Author)		
	blog=blogs(Title=Title,Blog=Article,Author=Author,Userid=Userid)
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

def read_my(request,category):
	if category == "all":
		new_dics={}
		all_blogs=blogs.objects.all()
		for blog in all_blogs:								
			str1=list_of_most_occured(blog.Blog)	
			res=fetch_result(str1,4)
			#print(str1,"\n related links")
			new_dics[blog.id]={'title':blog.Title,'Blog':blog.Blog,'Author':blog.Author,'Date':blog.Created_date,'Links':res}					
	elif category == "my":
		userid =request.session['userid']
		print(userid)
		new_dics={}
		try:
			all_blogs=blogs.objects.filter(Userid=userid)
		except:			
			all_blogs=None
		print(all_blogs)
		if all_blogs is not None:
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
		