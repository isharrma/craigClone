from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"base.html")

def new_search(request):
    search = request.POST.get("search")
    context = {
        'search' : search ,
    }
    return render(request,"Craiglist/new_search.html" ,context)