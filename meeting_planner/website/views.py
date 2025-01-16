from django.shortcuts import render
from django.http import HttpResponse
from meeting.models import Meeting, Room


# Create your views here.

def welcome_massage(request):
    return render(request, 'websites/index.html',
    {'meeting':Meeting.objects.all(),
     'room':Room.objects.all()})

def display_massage(request):
    return HttpResponse("An about page")