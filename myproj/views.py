# from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    # return HttpResponse("Hii Homepage")
    return render(request,"home.html")

def Aboutpage(request):
    # return HttpResponse("Hii Aboutt")
    return render(request,"about.html")