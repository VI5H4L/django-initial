from django.shortcuts import render

from .models import Post

# Create your views here.
def Postpage(request):
    # return HttpResponse("Hii Homepage")
    posts = Post.objects.all().order_by("-date") #ordered by date in desceneding order, used (-)
    print(posts)
    return render(request,"posts/posts_list.html",{"posts":posts})


