from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from .decorators import *

@unauthenticated_user
def signup(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request,'Account was successfully😊created happy reading ' +  user)
            return redirect('login')
        

    context={'form':form}
    return render(request,'entries/signup.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username of Password incorrect')


    context={}
    return render(request,"entries/login.html",context)


@login_required(login_url='login')
def index(request):
    entries=Entry.objects.order_by('-date_posted')
    context={"entries":entries}
    return render (request,"entries/index.html",context)

@login_required(login_url='login')
def add(request):
    if request.method=="POST":
        form=EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=EntryForm()
    context={"form":form}

    return render (request,"entries/add.html",context)

@login_required(login_url='login')
def fav(request):
    data = Entry.objects.filter(favorites=True)
        
    return render(request,"entries/favorites.html", {"data" : data})

@login_required(login_url='login')
def about(request):
    return render(request,"entries/about.html")

@login_required(login_url='login')
def topic(request):
    return render(request,"entries/topic.html")

def logoutUser(request):
    logout(request)
    return redirect('login')
