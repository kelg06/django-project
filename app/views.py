from django.shortcuts import render , redirect


from .forms import *





def index(request):
    entries=Entry.objects.order_by('-date_posted')
    context={"entries":entries}
    return render (request,"entries/index.html",context)


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


def fav(request):
    data = Entry.objects.filter(favorites=True)
        
    return render(request,"entries/favorites.html", {"data" : data})


def about(request):
    return render(request,"entries/about.html")


def topic(request):
    return render(request,"entries/topic.html")


