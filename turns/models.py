from django.db import models
from django.utils import timezone

class Turn(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    available = models.BooleanField(default=True)
    taken_by = models.TextField()

class Day(models.Model):
    id = models.IntegerField(primary_key=True)
    total_turns = models.IntegerField()
    disable_turns = models.IntegerField(default=False)
    taken_turns = models.IntegerField()
    untaken_turns = models.IntegerField()
    available = models.BooleanField(default=True)

class Week(models.Model):
    id = models.IntegerField(primary_key=True) # Number of the week per year. Range = [0,51]
    total_days = models.IntegerField()



