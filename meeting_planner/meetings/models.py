from django.db import models
from datetime import time

# Create your models here.
class Room(models.Model):
    name_room = models.CharField(max_length=100)
    number_floor = models.IntegerField()
    number_room = models.IntegerField()

    def __str__(self):
        return f"{self.name_room}: room {self.number_room} on floor {self.number_floor}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"