from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm

def index(request):
    #return HttpResponse('Hello World')
    meetups = Meetup.objects.all()
    context={'meetups':meetups}     #,'showmeetups':True} 
    return render(request,"meetups/index.html",context)

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        '''if request.method != 'POST':
            form = RegistrationForm()
            context={'meetup_found':True, 'selected_meetup':selected_meetup, 'form': form}
            return render(request, 'meetups/meetup-detail.html', context)
        else:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('all-meetups')
            context={'meetup_found':True, 'selected_meetup':selected_meetup, 'form': form}
            return render(request, 'meetups/meetup-detail.html', context)'''
        if request.method =='GET':
            form=RegistrationForm()
        else:
            form=RegistrationForm(request.POST)
            if form.is_valid():
                #participant = form.save()
                user_email=form.cleaned_data['email']
                participant, was_created = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                #return redirect(reverse('confirm_registration', kwargs={'meetup_slug':selected_meetup.slug}))
                return redirect('confirm_registration', meetup_slug=selected_meetup.slug)

        context={'meetup_found':True, 'selected_meetup':selected_meetup, 'form': form}
        return render(request, 'meetups/meetup-detail.html', context)
    except Exception as exc:
        print(exc)
        context = {'meetup_found': False}
        return render(request, 'meetups/meetup-detail.html', context)
    '''
    selected_meetup = get_object_or_404(Meetup, slug=meetup_slug)
    context={'selected_meetup':selected_meetup}
    return render(request, 'meetups/meetup-detail.html', context)'''


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    context={'meetup':meetup}
    return render(request, 'meetups/registration-success.html', context)