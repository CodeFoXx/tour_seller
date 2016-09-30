from django.db import models
from tours.models import Tour


class Consumer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return u'{}, {}, {}, {}'.format(self.name,self.surname,self.email, self.phone)


class Booking(models.Model):
    status = models.CharField(max_length=50)
    startDate = models.DateTimeField()
    finDate = models.DateTimeField()
    consumer = models.ForeignKey(Consumer)
    tour = models.ForeignKey(Tour)

    def __str__(self):
        return u'{}, {}, {}, {}, {}'.format(self.status,self.startDate,self.finDate, self.consumer,
                                            self.tour)


