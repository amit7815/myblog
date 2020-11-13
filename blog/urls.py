from django.contrib import admin
from django.urls import path
from blog.views1 import LoginView,SignupView,IndexView,logout
from . import views
from blog.middleware.login_required_middleware import login_required 
from blog.middleware.can_not_access_after_login import cantaccessafterlogin 

urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path('login',cantaccessafterlogin(LoginView.as_view()),name="login"),
    path('logout',logout,name="login"),
    path('blog/home',views.blogHome, name="blogHome"),
    path('blog/<int:id>/',login_required(views.blogPost),name='blogPost'),
    path('blog/create',login_required(views.BlogCreate.as_view(success_url="/"))),
    path('myblogs',login_required(views.myblog),name="myblog"),
    path('search/',login_required(views.search),name="search"),
    path('signup',cantaccessafterlogin(SignupView.as_view()),name="signup"),
   
]