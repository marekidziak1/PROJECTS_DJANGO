from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from . models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.utils import timezone
# Create your views here.
'''
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ','.join([q.question_text for q in question_list])
    #return HttpResponse(output)
    ###context = {'latest_question_list':question_list}
    ###template = loader.get_template('polls/index.html')
    ###return HttpResponse(template.render(context, request))
    context = {'latest_question_list':question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    ###try:
    ###    question = Question.objects.get(pk=question_id)
    ###except Question.DoesNotExist:
    ###    raise Http404("Qustion does not exist")
    ###return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = Question.objects.get(id=question_id)
    context ={'question':question}
    return render(request, 'polls/results.html', context)
'''
class IndexView(ListView):
    model=Question
    template_name='polls/index.html'
    context_object_name = 'latest_question_list'
    #queryset = Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
class DetailView(DetailView):
    model = Question
    template_name='polls/detail.html'
    context_object_name='question'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(DetailView):
    model = Question
    template_name='polls/results.html'
    context_object_name='question'

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = Question.objects.get(id=question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't choose"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', kwargs={"question_id":question.id}))
        #return render(request, 'polls/results.html', {'question':question})