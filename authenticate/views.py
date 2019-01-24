from django.shortcuts import render
from  django.http import HttpResponse,HttpResponseRedirect
from .models import User
from django.db.models import Q
from django.contrib import messages
from django import forms
# Create your views here.
def index(request):	
	return render(request,'base.html')

def login(request):
	if 'userid' in request.session:
		return HttpResponseRedirect('/blog/')
	return render(request,'login.html')

def register(request):
	if 'userid' in request.session:
		return HttpResponseRedirect('/blog/')
	return render(request,'signup.html',{})	

def createUser(request):
	if 'userid' in request.session:
		return HttpResponseRedirect('/blog/')
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
	if 'userid' in request.session:
		return HttpResponseRedirect('/blog/')
	userid=request.POST.get("userid")	
	password=request.POST.get("password")
	try:
		user=User.objects.get(Q(userId=userid)&Q(password=password))
	except:
		user=None
	if user is None:
		print("something wrong")
		messages.error(request,"Invalid credentials")				
	else:
		request.session['userid']=userid
		return	HttpResponseRedirect('/blog/')
	return render(request,'login.html',{})

def logout(request):
	if 'userid' in request.session:
		del request.session['userid']
		return HttpResponseRedirect('/')	
	return render(request,'login.html')