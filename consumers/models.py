from django.db import models


class Consumer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)


class Booking(models.Model):
    status = models.CharField(max_length=50)
    startDate = models.DateTimeField()
    finDate = models.DateTimeField()
    consumer = models.ForeignKey(Consumer)

