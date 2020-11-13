from django.views import View
from django.contrib.auth.hashers import check_password
from blog.models import User
from django.shortcuts import render,redirect
from django.contrib import messages


class LoginView(View):
    return_url=None
    def get(self, request):
        LoginView.return_url=request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            user = User.objects.get(name=name)
            print(user.name)
            flag = check_password(password=password, encoded=user.password)
            if flag:
                temp={}
                temp['name']=user.name;
                temp['id']=user.id;
                request.session['user']=temp;
                messages.success(request,"Successfully Logged in")
                if LoginView.return_url:
                    return redirect(LoginView.return_url)
                return redirect('/myblogs')
            else:
                return render(request, 'login.html', {'error': "username or password is invalid "})

        except:
            return render(request, 'login.html', {'error': "username or password is invalid "})
