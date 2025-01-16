from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from werkzeug.utils import redirect

from meeting.models import Meeting, Room



# Create your views here.

def detail(request, id):
    #meeting = Meeting.objects.get(pk = id)
    #meeting = get_object_or_404(Meeting, pk=id)
    meeting = Meeting.objects.all()
    return render(request, 'meetings/detail.html',
    {'meeting': meeting})

def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, 'meetings/detail.html',
                  {'room': room})

MeetingForm = modelform_factory(Meeting, exclude = [])

def new_room(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome_massage')
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html',
                      {'form':form})

