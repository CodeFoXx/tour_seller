from django.db import models
from django.contrib.auth.models import User, UserManager
from tours.models import Tour
from datetime import datetime, timedelta, timezone

allTours = Tour.objects.all()


def get_deadline():
    return datetime.utcnow() + timedelta(days=1)


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


class Status(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return u'{}'.format(self.status)


# obj1 = Status.create("заявлен на бронь")
# obj2 = Status.create("бронь подтверждена")
# obj3 = Status.create("бронь отклонена")
# obj4 = Status.create("заявлен на покупку")
# obj5 = Status.create("покупка подтверждена")
# obj6 = Status.create("покупка отклонена")


class Booking(models.Model):
    status = models.ForeignKey(Status, null=True)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    fin_date = models.DateTimeField(default=get_deadline)
    amount_of_people = models.PositiveIntegerField(default=1)
    consumer = models.ForeignKey(Consumer, null=True)
    tour = models.ForeignKey(Tour, null=True)
    final_cost = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.tour:
            self.final_cost = self.tour.price * self.amount_of_people
        super(Booking, self).save(*args, **kwargs)

    def price(self):
        cs = self.amount_of_people * self.tour.price
        return cs

    def __str__(self):
        return u'{}, ({:%d-%m-%Y} - {:%d-%m-%Y}), {}, {}'.format(self.status, self.start_date, self.fin_date, self.consumer.name,
                                            self.tour.name)


class Buying(models.Model):
    status = models.ForeignKey(Status, null=True)
    buy_date = models.DateTimeField(default=datetime.now, blank=True)
    amount_of_people = models.PositiveIntegerField(default=1)
    consumer = models.ForeignKey(Consumer, null=True)
    tour = models.ForeignKey(Tour, null=True)
    final_cost = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.tour:
            self.final_cost = self.tour.price*self.amount_of_people
        super(Buying, self).save(*args, **kwargs)

    def price(self):
        cs = self.amount_of_people * self.tour.price
        return cs

    def __str__(self):
        return u'{}, ({:%d-%m-%Y}), {} руб, {}, {}'.format(self.status, self.buy_date, self.final_cost, self.consumer.name,
                                            self.tour.name)

