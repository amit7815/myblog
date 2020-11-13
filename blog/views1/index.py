from django.shortcuts import render, HttpResponse,redirect
from blog.models import User
# from shop.utils.email_sender import sendEmail
# import random
# import math
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        
        return render(request, 'index.html')


def logout(request):
    request.session.clear();
    messages.success(request,"successfully logged out !")
    return redirect('/login')

    