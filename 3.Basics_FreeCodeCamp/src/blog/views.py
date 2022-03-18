from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article

class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.all()  


class ArticleDetailView(DetailView):
    model = Article
    template_name='blog/article_detail.html'
    
    #pobranie obiektu 
    def get_object(self):
        my_id = self.kwargs.get("pk")                      #pk pobrane ze ścieżki url <int:pk> (podajesz pk bo tak jest w ściezce/linku)
        return get_object_or_404(Article, pk =my_id)       #musisz podać id albo pk

from .forms import ArticleForm
class ArticleCreateView( LoginRequiredMixin, CreateView):
    model = Article
    queryset = Article.objects.all()   
    #fields=['title', 'content', 'active']
    form_class = ArticleForm
    def get_success_url(self):
        return super().get_success_url() #return '/'
    def form_valid(self, form):
        return super().form_valid(form)

class ArticleUpdateView( LoginRequiredMixin, UpdateView):
    model = Article
    #fields=['title', 'content', 'active']
    form_class = ArticleForm    
    def get_object(self):
        my_id = self.kwargs.get("pk")    
        return get_object_or_404(Article, pk =my_id)      
    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'pk':self.get_object().id}) 

class ArticleDeleteView( LoginRequiredMixin, DeleteView):
    model = Article
    def get_success_url(self):
        return reverse('blog:article-list' ) #return '/' 
    def get_object(self):
        my_id = self.kwargs.get("pk")                       #pk pobrane ze ścieżki url <int:pk> (podajesz pk bo tak jest w ściezce/linku)
        return get_object_or_404(Article, pk =my_id)        #musisz podać id albo pk 