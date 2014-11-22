from django.db import models

class Event(models.Model):
    name = models.TextField()
    desc = models.TextField()
    url = models.URLField()
    TYPE_TRIP = 'TR'
    TYPE_COMPETITION = 'CO'
    TYPE_TALK = 'TA'
    TYPE_CHOICES = (
        (TYPE_TRIP, 'trip'),
        (TYPE_COMPETITION, 'competition'),
        (TYPE_TALK, 'talk'),
    )
    start = models.DateField()
    end = models.DateField()
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    location = models.CharField(max_length=100)

class Trip(Event):
    cost = models.DecimalField(decimal_places=2, max_digits=14)

class Competition(Event):
    rewards = models.CharField(max_length=100)
