from django.db import models
from tours.models import Tour


class Booking(models.Model, list):
    status = models.CharField(max_length=50)
    startDate = models.DateTimeField()
    finDate = models.DateTimeField()
    bookedTours = models.ForeignKey(list(Tour))


class Consumer(models.Model, list):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    tourCart = models.ForeignKey(list(Booking))


