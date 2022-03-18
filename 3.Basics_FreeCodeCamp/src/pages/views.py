from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args,**kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    context = {
        "my_text":"this is about us",
        "my_number":[1,2,3]
    }
    return render(request, "home.html", context)

def about_view(request, *args,**kwargs):
    context = {
        "list":[11,12,'abc', 12312]
    }
    return render(request, "about.html", context)
