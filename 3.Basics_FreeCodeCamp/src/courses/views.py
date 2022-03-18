from django.shortcuts import render, redirect,  get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from .models import Course
from .forms import CourseModelForm


class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj=get_object_or_404(self.model, id=id)
        return obj


#BASE VIEW CLASS 
#ListView
class CourseListView(View):
    template_name = 'courses/course_list.html'
    #GET METHOD
    def get(self, request, *args, **kwargs):
        obj_lst=Course.objects.all()
        context={'object_list': obj_lst}
        return render(request, self.template_name, context) 

#DetailView
class CourseDetailView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    #GET METHOD
    def get(self, request, pk=None, *args, **kwargs):       
        context={}
        if pk is not None:
            obj=self.get_object()
            #obj = get_object_or_404(Course, id=pk)
            context = {'object':obj}
        return render(request, self.template_name, context)

 #CreateView
class CourseCreateView(View):
    template_name = "courses/course_form.html"
    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context ={'form': form} 
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs): 
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('courses:course_detail', kwargs={'pk':form.instance.id}))
        context ={'form':form}  
        return render(request, self.template_name, context)

 #UpdateView
class CourseUpdateView(View):
    template_name = "courses/course_form.html"
    def get_object(self):
        id=self.kwargs.get('pk')
        obj = None
        if id is not None:
            obj=get_object_or_404(Course, id=id)
        return obj
    def get(self, request,pk=None, *args, **kwargs):
        form = CourseModelForm()
        if pk is not None:
            obj = get_object_or_404(Course, id=pk) 
            form= CourseModelForm(instance=obj)
        context ={'form': form} 
        return render(request, self.template_name, context)
    #POST METHOD 
    def post(self, request, pk=None, *args, **kwargs): 
        context={}
        if pk is not None:
            form = CourseModelForm(request.POST, instance=get_object_or_404(Course, id=pk))
            if form.is_valid():
                form.save()
                return redirect(reverse('courses:course_detail', kwargs={'pk':form.instance.id}))
            context ={'form':form}  
            return render(request, self.template_name, context)

class CourseDeleteView(View):
    template_name = "courses/course_form.html"
    def get_object(self):
        id=self.kwargs.get('pk')
        obj = None
        if id is not None:
            obj=get_object_or_404(Course, id=id)
        return obj
    def get(self, request,pk=None, *args, **kwargs):
        obj = get_object_or_404(Course, id=pk) 
        context ={'object': obj} 
        return render(request, self.template_name, context)
    #POST METHOD 
    def post(self, request, pk=None, *args, **kwargs): 
        obj= get_object_or_404(Course, id=pk)
        context={}
        if obj is not None:
            obj.delete() 
            return redirect('/')
        return render(request, self.template_name, context)


#HTTP METHOD:
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})