from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import blogs
from django.http import HttpResponse,HttpResponseRedirect
from .service.Googlesearch import fetch_result
from .service.MostOccured import list_of_most_occured
from django.contrib import messages
from PIL import Image

def index(request):
	if 'userid' not in request.session:
		messages.error(request,'You need to login first')
		return HttpResponseRedirect("/authenticate/login")
	return render(request,'blog_menu.html',{})
	
def addblog(request):
	if 'userid' not in request.session:
		messages.error(request,'You need to login first')
		return HttpResponseRedirect("/authenticate/login")
	return render(request,'addblog.html',{})


def save(request):
	if 'userid' not in request.session:
		messages.error(request,'You need to login first')
		return HttpResponseRedirect("/")	
	Author=request.POST.get('author')
	Title=request.POST.get('title')
	Article=request.POST.get('article')
	Img=request.FILES.get('image')
	Userid=request.session['userid']
	print("Image name = ",Img.name)	
	#Img.save()
	#print(Author)		
	blog=blogs(Title=Title,Blog=Article,Author=Author,Userid=Userid,Image=Img)
	blog.save()
	return HttpResponseRedirect("/")


def read(request):
	if 'userid' not in request.session:
		messages.error(request,'You need to login first')
		return HttpResponseRedirect("/authenticate/login")
	new_dics={}
	all_blogs=blogs.objects.all()
	for blog in all_blogs:								
		str1=list_of_most_occured(blog.Blog)	
		res=fetch_result(str1,4)
		#print(str1,"\n related links")
		print(blog.Title)
		print(blog.Image)
		new_dics[blog.id]={'image':blog.Image,'title':blog.Title,'Blog':blog.Blog,'Author':blog.Author,'Date':blog.Created_date,'Links':res}					
		'''
		for key,value in res.items():
			if key =="":
				continue
			try:
				new_dics[blog.id][key]=value
			except:
				continue
		'''
	#print(new_dics)	
	return render(request,"readblogs.html",{'Blogs':new_dics})

def read_my(request,category):
	if 'userid' not in request.session:
		messages.error(request,'You need to login first')
		return HttpResponseRedirect("/authenticate/login")
	if category == "all":
		new_dics={}
		all_blogs=blogs.objects.all()
		for blog in all_blogs:								
			str1=list_of_most_occured(blog.Blog)	
			res=fetch_result(str1,4)
			#print(str1,"\n related links")
			img=str(blog.Image)
			img_url=img[7:]
			print(img_url)	

			new_dics[blog.id]={'image':img_url,'title':blog.Title,'Blog':blog.Blog,'Author':blog.Author,'Date':blog.Created_date,'Links':res}					
	elif category == "my":
		userid =request.session['userid']
		#print(userid)
		new_dics={}
		try:
			all_blogs=blogs.objects.filter(Userid=userid)
		except:			
			all_blogs=None
		#print(all_blogs)
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
	#print(new_dics)	
	return render(request,"readblogs.html",{'Blogs':new_dics})


class Blogs_view(CreateView):	
	model=blogs
	fields=['Title','Blog','Author']
		