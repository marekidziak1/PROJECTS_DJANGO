from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request): 
    #return HttpResponse('Hello World')
    x=1
    y=2
    return render(request, 'helloHTML.html',{'name':'Mosh'})