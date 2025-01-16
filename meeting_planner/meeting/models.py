from django.db import models
from datetime import time


# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f'{self.room_name} {self.room_number} an {self.floor_number}'


class Meeting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} at {self.start_time} on {self.date}'


