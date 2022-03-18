

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import Room, Topic, Message
from django.db.models import Q
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
def loginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        else:
            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'username or password does not exist')
    context={'page':page}                              #if request.method=="POST":
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    #page='register'
    form = UserCreationForm()
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, "You've created an account")
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')
    context={'form': form}
    return render(request, 'base/login_register.html', context)

def home(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains= q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q))
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages =Message.objects.filter(
        Q(room__topic__name__icontains=q) |
        Q(room__name__icontains=q) |
        Q(user__username__icontains=q) |
        Q(body__icontains= q))

    context = {'rooms':rooms, 'topics': topics, 'room_count':room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html',context)

def room(request, pk):
    room=Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    room_participants = room.participants.all()
    if request.method=="POST":
        message=Message.objects.create(
            user = request.user,
            room=room,
            body= request.POST.get("body")
        )
        room.participants.add(request.user)
        return redirect('room-detail', pk=room.id )
    context={'room':room, 'room_messages':room_messages, 'participants':room_participants}
    return render(request,'base/room.html', context)

def userProfile(request,pk):
    context={}
    try:
        user_chosen = User.objects.get(id=pk)
    except:
        messages.error(request,'User does not exist')
    else:
        rooms= user_chosen.room_set.all()
        room_messages = user_chosen.message_set.all()
        topics=[]
        for r in rooms:
            if r.topic not in topics:
                topics.append(r.topic)
        context={'user_chosen':user_chosen, 'rooms':rooms, 'room_messages':room_messages, 'topics':topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room=Room.objects.get(id=pk)
    form = RoomForm(instance = room)
    if request.user != room.host :
        return HttpResponse('You are not allowed here')
    if request.method == "POST":
        form=RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room=Room.objects.get(id=pk)
    if request.user != room.host :
        return HttpResponse('You are not allowed here')
    if request.method=='POST':
        room.delete()
        return redirect('home')
    context = {'obj':room}
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def deleteMessage(request, pk):
    message=Message.objects.get(id=pk)
    if request.user != message.user :
        return HttpResponse('You are not allowed here')
    if request.method=='POST':
        message.delete()
        messages.success(request,"You've successfully delete a message")
        return redirect('home')
    context = {'obj':message}
    return render(request, 'base/delete.html', context)

