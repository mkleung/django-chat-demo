from django.db.models import F
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Room, Question, Topic
from .forms import RoomForm
from django.template import loader
from django.db.models import Q

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn English'},
#     {'id': 2, 'name': 'Lets learn Spanish'},
#     {'id': 3, 'name': 'Lets learn French'},
# ]


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms' : rooms, 'topics': topics, 'room_count': room_count}
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


# Details

def polls(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "chatapp/poll/polls.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "chatapp/poll/detail.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "chatapp/poll/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        return render(request, "chatapp/poll/results.html", {"question": question})
    
    

    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "chatapp/poll/results.html", {"question": question})