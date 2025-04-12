from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn English'},
#     {'id': 2, 'name': 'Lets learn Spanish'},
#     {'id': 3, 'name': 'Lets learn French'},
# ]


def home(request):
    rooms = Room.objects.all()
    
    context = {'rooms' : rooms}
    return render(request, 'chatapp/home.html', context)


def about(request):
    return render(request, "chatapp/about.html")


def room(request, pk):
    # return one single item. pk is primary key
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'chatapp/room.html',  context) 