from django.shortcuts import render

# Create your views here.
def Postpage(request):
    # return HttpResponse("Hii Homepage")
    return render(request,"posts/posts_list.html")


