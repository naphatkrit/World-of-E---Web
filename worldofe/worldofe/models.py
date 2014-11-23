from django.db import models

# We use multi-table inheritance. See: https://docs.djangoproject.com/en/1.7/topics/db/models/#multi-table-inheritance

class Organizer(models.Model):
    name = models.TextField()

class Company(Organizer):
    url = models.URLField()

class Student_Organization(Organizer):
    pass

class Event(models.Model):
    name = models.TextField()
    desc = models.TextField()
    url = models.URLField()
    TYPE_TRIP = 'TR'
    TYPE_COMPETITION = 'CO'
    TYPE_TALK = 'TA'
    TYPE_RECRUITING = 'RE'
    TYPE_CHOICES = (
        (TYPE_TRIP, 'trip'),
        (TYPE_COMPETITION, 'competition'),
        (TYPE_TALK, 'talk'),
        (TYPE_RECRUITING, 'recruiting'),
    )
    start = models.DateField()
    end = models.DateField()
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(Organizer)

    STATUS_APPROVED = 'AP'
    STATUS_REJECTED = 'RE'
    STATUS_PENDING = 'PE'
    STATUS_CHOICES = (
        (STATUS_APPROVED, 'approved'),
        (STATUS_REJECTED, 'rejected'),
        (STATUS_PENDING, 'pending'),
    )
    approval_status = models.CharField(max_length=2, choices=STATUS_CHOICES)

class Trip(Event):
    cost = models.DecimalField(decimal_places=2, max_digits=14)

class Competition(Event):
    rewards = models.CharField(max_length=100)
