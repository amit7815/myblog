from django.views import View
from django.contrib.auth.hashers import check_password,make_password
from blog.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from captcha.image import ImageCaptcha
from captcha.fields import CaptchaField
from blog.forms import signUpForm

class SignupView(View):
    def get(self, request):
        # image_captcha = ImageCaptcha()
        form=signUpForm()
        # image = image_captcha.generate_image('1234')
        return render(request,'signup.html',{'form':form})

    def post(self, request):
        print(request.POST)
        form=signUpForm(request.POST)
        try:

           # print(request.POST)
            user=None
            name = request.POST.get('username')
            try:
                user=User.objects.get(name=name)
            except:
                user=None
            if user is not None:
                return render(request, 'signup.html', {'form':form,'error': "This username already exists try another username"})


            print()
            # email = request.POST.get('email')
            if len(name)<6:
                return render(request, 'signup.html', {'form':form,'error': "username must be greater than 6 character"})
                
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            if len(password)<8 or not password.isalnum():
                return render(request, 'signup.html', {'form':form,'error': "password must be greater than 8 character and alphanumeric"})
            
            if len(repassword)<8 or not repassword.isalnum():
                return render(request, 'signup.html', {'form':form,'error': "confirm password must be greater than 8 character and alphanumeric"})
            
            if password!=repassword:
                return render(request, 'signup.html', {'form':form,'error': "Password not matched"})
            hashedpassword=make_password(password)
            user = User(name=name, password=hashedpassword)
            
            print(user)
            if form.is_valid():
                human=True
                user.save()
                messages.success(request,"Your acccount created successfully login now")
                return render(request, 'login.html')
            else:
                return render(request,"signup.html",{"form":form, "error":"invalid captcha"})
        except:
            pass
