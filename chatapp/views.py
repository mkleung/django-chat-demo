from django.db.models import F
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Room, Topic, Message
from .forms import RoomForm
from django.template import loader
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    
    context = {
        'rooms' : rooms, 
        'topics': topics, 
        'room_count': room_count, 
        'room_messages': room_messages,
        'q': q,
        }
    return render(request, 'chatapp/home.html', context)


def about(request):
    return render(request, "chatapp/about.html")


# Rooms

def room(request, pk):
    room = Room.objects.get(id=pk)
    
    # give me a list of messages that are related to this room
    room_messages = room.message_set.all()
    
    participants = room.participants.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    
    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'chatapp/room.html',  context) 

@login_required(login_url='login')
def createRoom(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid(): 
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            form.save() 
            return redirect('home')
    else:
        form = RoomForm()  
    return render(request, "chatapp/room_form.html", {'form': form})



@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host :
        return HttpResponse('You are not allowed on this page')

    # Edits the form
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'chatapp/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    deleteRoom = Room.objects.get(id=pk)
    
    if request.user != room.host :
        return HttpResponse('You are not allowed on this page')

    item = get_object_or_404(Room, id=pk)
    item.delete()
    
    rooms = Room.objects.all()

    context = {'deleteRoom' : deleteRoom, 'rooms': rooms}
    return render(request, 'chatapp/home.html', context)


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user :
        return HttpResponse('You are not allowed on this page')

    if request.method == 'POST':
        message.delete()
        return redirect('home')

    return render(request, 'chatapp/delete.html', {'obj': message})




# Authentication
def loginPage(request):
    
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    context = {'page': page}
    return render(request, 'chatapp/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
            
    return render(request, 'chatapp/login_register.html', {'form': form})


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages= user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'chatapp/profile.html', context)