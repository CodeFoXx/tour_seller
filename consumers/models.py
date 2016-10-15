from django.db import models
from django.contrib.auth.models import User, UserManager
from tours.models import Tour

class ConsumerManager(models.Manager):
    def create_consumer(self, email, password):
        user = self.create(email=email, password=password)
        # do something with the book
        return user

class Consumer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=11,default="")
    objects = ConsumerManager()

    def __str__(self):
        return u'{}, {}, {}, {}'.format(self.name, self.surname, self.email, self.phone)





# class NewConsumer(User):
#     phone = models.CharField(max_length=11)
#     object = UserManager()
#     user = Consumer.objects.create()


class Booking(models.Model):
    status = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    fin_date = models.DateTimeField()
    consumer = models.ForeignKey(Consumer, null=True)
    tour = models.ForeignKey(Tour, null=True)

    def __str__(self):
        return u'{}, {}, {}, {}, {}'.format(self.status, self.start_date, self.fin_date, self.consumer,
                                            self.tour)
