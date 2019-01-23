from django.shortcuts import render
from  django.http import HttpResponse,HttpResponseRedirect
from .models import User
from django.db.models import Q

# Create your views here.
def index(request):	
	return render(request,'base.html')

def login(request):
	return render(request,'login.html')

def register(request):
	return render(request,'signup.html',{})	

def createUser(request):
	username=request.POST.get("username")
	print(username)
	userid=request.POST.get("userid")
	print(userid)
	dob=request.POST.get("dob")
	print(dob)
	password=request.POST.get("password")
	print(password)
	new_user=User(username=username,userId=userid,dob=dob,password=password)
	new_user.save()
	return	HttpResponseRedirect('/')

def login_User(request):
	userid=request.POST.get("userid")	
	password=request.POST.get("password")
	try:
		user=User.objects.get(Q(userId=userid)&Q(password=password))
	except:
		user=None
	if user is None:
		return	HttpResponseRedirect('/authenticate/login')
	else:
		return	HttpResponseRedirect('/')
	return	HttpResponseRedirect('/')