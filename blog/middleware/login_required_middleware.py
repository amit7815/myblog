from django.shortcuts import render,redirect
from django.contrib import messages
def login_required(get_response):
    def middleware(request,id=None):
        print("middleware.....")
        user=request.session.get('user')
       
        if user:
            response=None
            if id:
                response=get_response(request,id)
            else:
                response=get_response(request)
            return response
        else:
            print("please login")
            url=request.path
            print(url)
            messages.error(request,"please login")
            return redirect(f"/login?return_url={url}")


    return middleware