from django.contrib import admin
from django.urls import path

from website.views import welcome_massage, display_massage
from meeting.views import detail, room_detail, new_room

urlpatterns = [
    path('meeting/<int:id>', detail, name = 'detail'),
    path('room/<int:id>', room_detail, name = 'room_detail'),
    path('new_meeting', new_room, name = 'new_room'),
]