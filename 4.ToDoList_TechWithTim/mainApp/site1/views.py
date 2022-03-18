from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect 
from .models import Item, ToDoList
from django.contrib.auth.models import User
from .forms import CreateNewList, CreateNewItem
# Create your views here.
#def index(response,id):
    #return HttpResponse("<h1>tech with tim</h1>")


def index(request,id):
    lst = ToDoList.objects.get(id=id)
    if lst in request.user.todolist_set.all():
        if request.method != 'POST':
            context ={'ls':lst}
            return render(request, "site1/list.html", context)
        else:                           #if request.method == 'POST':
            print(request.POST)
            if request.POST.get("saveButton"):
                for item in lst.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif request.POST.get("saveNewItemButton"):
                txt = request.POST.get("new")
                if len(txt)>2:
                    lst.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
            context ={'ls':lst}
            return render(request, "site1/list.html", context)
    return render(request, "site1/home.html", context)














def home(response):
    return render(response, "site1/home.html", {'name':'test'})
    
def list(response,id):
    lst = ToDoList.objects.get(id=id)
    context ={'ls':lst}
    return render(response, "site1/list.html", context)

def create(request):
    if request.method =='POST':
        form = CreateNewList(request.POST)
        if form.is_valid():
            t= ToDoList(name=form.cleaned_data["name"])
            t.save()
            request.user.todolist.add(t)
            #return redirect(reverse('list',kwargs = {'id':t.id}))
            return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    context={'form':form}
    return render(request, "site1/create.html", context)

def view(request):
    context={}
    if request.user.is_authenticated:
        t = request.user.todolist_set.all()
        context ={'my_list':t}
    return render(request, "site1/view.html", context)




def v1(response, my_pk):
    return HttpResponse("%s " % my_pk)

def v3(response, my_name):
    t1 = ToDoList.objects.get(name=my_name)
    item = t1.item_set.get(id=1)
    return HttpResponse("%s %s" %(t1.name, str(item.text)))

def v2(response, my_pk):	
    obj = Item.objects.get(id=my_pk)
    return HttpResponse("%s" % obj.id)