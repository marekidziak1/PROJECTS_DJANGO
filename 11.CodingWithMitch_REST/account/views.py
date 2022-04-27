from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Account

def home(request):
    return render(request, 'account/home.html')
# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user = Account.objects.get(email=email)
        except:
            messages.error(request, 'email does not exist')
        else:
            user=authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                print('log in')
                messages.success(request, 'log in successful')
                return redirect('home')
            else:
                messages.error(request, 'username or password does not exist')
    return render(request, 'account/login.html')

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        print('log out')
        messages.success(request, 'log out successful')
    return redirect('home')
