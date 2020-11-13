from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views.generic.edit import CreateView 
from blog.models import Blog
from blog.models import User
from django.contrib import messages



# Create your views here.
class BlogCreate(CreateView):
    model=Blog
    fields=['pic','title','content']
    def form_valid(self, form):
        # print(self.request.session['user'].get('name'))
        user=User.objects.get(id=self.request.session['user'].get('id'))
        self.object=form.save()
        self.object.user=user
        self.object.save()
        messages.success(self.request,"Your Blog created successfully")
        return HttpResponseRedirect("/myblogs")




# Create your views here.
def blogHome(request):
    allPosts=Blog.objects.all()
    # posts=Blog.objects.filter(user=User.objects.get(name=request.session['user'].get('name')))
    # print(allPosts)
    context={"allPosts":allPosts}
    return render(request,"blogHome.html",context)

def myblog(request):
    posts=Blog.objects.filter(user=User.objects.get(name=request.session['user'].get('name')))
    # print(allPosts)
    context={'posts':posts}
    return render(request,"myblog.html",context)

def blogPost(request,id):
    post=Blog.objects.filter(sno=id).first() #or [0]
    #print(post)
    # comment corresponding to this post
    # comments=BlogComment.objects.filter(post=post,parent=None)
    # replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    # replyDict={}
    print(request.session['user'])
    user=User.objects.get(id=request.session['user'].get('id'))
    print(user)
    

    context={"post":post,'user':user}
    return render(request,"blogPost.html",context)


        
   




# Create your views here.
# @login_required(redirect_field_name='settings.LOGIN_URL')




# @login_required(redirect_field_name='settings.LOGIN_URL')
def search(request):
    query=request.GET['query']
    allPostUser=None
    user=None
    if len(query)>78:
        allPosts=Blog.objects.none()  #how to create empty queryset in django
    # allPosts=Post.objects.all()
    else:
        try:
            user=User.objects.get(name=query)
            allPostsTitle=Blog.objects.filter(title__icontains=query)
            allPostsContent=Blog.objects.filter(content__icontains=query)
        except:
            allPostsTitle=Blog.objects.filter(title__icontains=query)
            allPostsContent=Blog.objects.filter(content__icontains=query)
        
        if user is not None:
            allPostsUser=Blog.objects.filter(user=user)
        #merge two queryset
            allPosts1=allPostsTitle.union(allPostsContent)
            allPosts=allPosts1.union(allPostsUser)
        else:
            allPosts=allPostsTitle.union(allPostsContent)
        
    if allPosts.count()==0: # how to find length of queryset in django
        messages.error(request,"No search results found please refine your query")
    params={"allPosts":allPosts,"query":query}
    return render(request,'search.html',params)






