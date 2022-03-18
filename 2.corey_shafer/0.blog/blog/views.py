from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.contrib.messages.api import success
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Post
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
'''
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
'''
class PostListView(ListView):
    model=Post
    template_name='blog/home.html' 
                 #default looks for: 
                 #<app>/<model>_<viewstype>.html'
    context_object_name='posts'
                 #default object_name
    ordering=['-date_posted']
    paginate_by=5 

class PostDetailView(DetailView):
    model=Post
    pk_url_kwarg = 'pk'
 
class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title', 'content']
    #success_url='/about/' #zamiast tego to w modelu Post przeciążasz metdoę get_url()
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

