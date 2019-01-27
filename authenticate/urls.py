from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name="index"),
path('register/',views.register,name="register"),
path('login/',views.login,name="login"),
path('signup/',views.createUser,name="signup"),
path('login_user/',views.login_User,name="login_user"),
path('logout/',views.logout,name="logout"),
]