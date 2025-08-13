from django.shortcuts import render, HttpResponse
from .models import Room
# rooms = [
#     {'id': 1, 'name': 'HTML Basics'},
#     {'id': 2, 'name': 'CSS Fundamentals'},
#     {'id': 3, 'name': 'JavaScript Essentials'},
# ]
 

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/index.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

