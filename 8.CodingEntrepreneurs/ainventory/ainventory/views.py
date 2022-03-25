from django.http import HttpResponse
from articles.models import Article
'''
article_obj = Article.objects.get(id=2)
HTML_STRING=f"<h1>{article_obj.title}</h1><hr/><h1>{article_obj.content}</h1>"
def home(request):
    return HttpResponse(HTML_STRING)
'''
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
def home(request):
    article_objects = Article.objects.all()
    context={'article_obj':Article.objects.get(id=2),
             'my_lst' :article_objects,
            }
    HTML_String = render_to_string('home-view.html', context)
    return HttpResponse(HTML_String)
    #return render(request, 'home-view.html', context)
