from django.shortcuts import render, HttpResponse, redirect 
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm
# rooms = [
#     {'id': 1, 'name': 'HTML Basics'},
#     {'id': 2, 'name': 'CSS Fundamentals'},
#     {'id': 3, 'name': 'JavaScript Essentials'},
# ]
 

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) | 
        Q(description__icontains=q)

    )
    topics = Topic.objects.all()
    rooms_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'rooms_count': rooms_count}
    return render(request, 'base/index.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':    
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form} 
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':    
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render (request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})