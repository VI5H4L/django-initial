from django.shortcuts import render,redirect

# To use forms from django 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save() saves user in admin and also gives the user which we are using to login
            login(request,form.save())
            return redirect("posts:list")
    else:  #GET REQUEST 
        form = UserCreationForm()

    return render(request,"users/register.html",{'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #LOGIN HERE
            login(request, form.get_user())
            if 'next' in request.POST :
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")       
    else: #GET REQUEST 
        form = AuthenticationForm()

    return render(request,"users/login.html",{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("posts:list")