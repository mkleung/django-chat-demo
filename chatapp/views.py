from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn English'},
    {'id': 2, 'name': 'Lets learn Spanish'},
    {'id': 3, 'name': 'Lets learn French'},
]


def home(request):
    context = {'rooms' : rooms}
    return render(request, 'chatapp/home.html', context)


def about(request):
    return render(request, "chatapp/about.html")


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    
    context = {'room': room}

    return render(request, 'chatapp/room.html',  context) 