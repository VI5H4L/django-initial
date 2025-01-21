from django.shortcuts import render
# from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Post

# Create your views here.
def posts_list(request):
    # return HttpResponse("Hii Homepage")
    posts = Post.objects.all().order_by("-date") #ordered by date in desceneding order, used (-)
    # print(posts)
    return render(request,"posts/posts_list.html",{"posts":posts})

def post_page(request,slug):
    post = Post.objects.get(slug = slug)
    return render(request,"posts/post_page.html",{"post":post})

@login_required(login_url="/users/login")
def post_new(request):
    return render(request,"posts/post_new.html")