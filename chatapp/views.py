from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

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


def createRoom(request):

    # Handle Form
    if request.method == "POST":
        form = RoomForm(request.POST)  # Pass POST data to the form
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = RoomForm()  

    return render(request, "chatapp/room_form.html", {'form': form})


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    # Edits the form
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'chatapp/room_form.html', context)


def deleteRoom(request, pk):
    deleteRoom = Room.objects.get(id=pk)

    item = get_object_or_404(Room, id=pk)
    item.delete()
    
    rooms = Room.objects.all()

    context = {'deleteRoom' : deleteRoom, 'rooms': rooms}
    return render(request, 'chatapp/home.html', context)