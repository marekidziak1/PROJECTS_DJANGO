from django.shortcuts import render, redirect
from .models import Article
from django.db.models import Q
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required
from . forms import ArticleForm

from django.contrib.auth.forms import UserCreationForm

def home_view(request, id):
    article_objects = Article.objects.all()
    context={'article_obj':Article.objects.get(id=2),
             'my_lst' :article_objects,
            }
    HTML_String = render_to_string('home-view.html', context)
    return HttpResponse(HTML_String)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context ={
        "object":article_obj,
    }
    return render(request, "articles/detail.html", context)

def article_search_view(request):
    print(dir(request))
    if request.method == "GET":
        my_q = request.GET.get('q') 
        objects= Article.objects.filter(Q(title__icontains=my_q) | Q(content__icontains=my_q)) if my_q != None else None
    if request.method == "POST":
        my_abc = request.POST.get('abc')
        objects= Article.objects.filter(Q(title__icontains=my_abc) | Q(content__icontains=my_abc))
    context={'objects' :objects}
    return render(request, "articles/searched.html", context)

@login_required
def article_create_view(request):
    context={
        'form':ArticleForm()
    }
    if request.method == "POST":
    #basic HTML FORM
        # my_title=request.POST.get("form_title")
        # my_content=request.POST.get("form_content")
        # my_article, was_created = Article.objects.get_or_create(title=my_title)
        # if was_created:
        #     my_article.content=my_content
        #     my_article.save()
        #     return redirect('home')
        # context={'article':my_article}

    #ArticleForm  (forms.Form)
        # form = ArticleForm(request.POST)
        # if form.is_valid():
        #     my_title=form.cleaned_data.get("title")
        #     my_content=form.cleaned_data.get("content")
        #     my_article, was_created = Article.objects.get_or_create(title=my_title)
        #     if was_created:
        #         my_article.content=my_content
        #         my_article.save()
        #         return HttpResponseRedirect(reverse('home'))
        # context={'form':form}

    #ArticleForm  (forms.ModelForm)
        form = ArticleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('title'))
            form.save()
            return HttpResponseRedirect(reverse('home'))
            # my_title=request.POST.get("title")
            # my_content=request.POST.get("content")
            # my_article, was_created = Article.objects.get_or_create(title=my_title)
            # if was_created:
            #     my_article.content=my_content
            #     my_article.save()
            #     return HttpResponseRedirect(reverse('home'))
        context={'form':form}
    return render(request, "articles/create.html", context)

def login_view(request):
    context={}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    if request.method =="POST":
        my_username=request.POST.get('username')
        my_password=request.POST.get('password')
        my_email=request.POST.get('email')
        if len(my_username) >3 and len(my_password) and '@' in my_email :
            flag=False
            for user in User.objects.all():
                flag =True if user.username == my_username and user.email == my_email else None                    
            if flag: 
                user = authenticate(request, username=my_username, password = my_password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
        context={'my_username':my_username, 'my_email' :my_email}    
    return render(request, 'accounts/login.html', context=context)

def searched_view(request):
    context={}
    return render(request, 'articles/searched.html', context)