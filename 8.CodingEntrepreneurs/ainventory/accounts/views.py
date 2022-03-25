from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def login_view(request):
    context={}
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context={"error": 'Invalid username or password'}
    return render(request, "accounts/login.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return render(request, "accounts/logout.html", {})

def register_view(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        login(request, user_obj)
        return redirect('home')
    context={'form':form}
    return render(request, 'accounts/register.html', context)