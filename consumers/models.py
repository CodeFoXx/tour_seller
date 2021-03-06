from datetime import datetime, timedelta, time

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

from tours.models import Tour
import warnings

warnings.filterwarnings(
    'ignore', r"DateTimeField .* received a naive datetime",
    RuntimeWarning, r'django\.db\.models\.fields')

allTours = Tour.objects.all()


def get_deadline():
    return datetime.now() + timedelta(minutes=10)


class Status(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return u'{}'.format(self.status)


class Booking(models.Model):
    status = models.ForeignKey(Status, null=True)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    fin_date = models.DateTimeField(default=get_deadline)
    amount_of_people = models.PositiveIntegerField(default=1)
    consumer = models.ForeignKey(User, null=True)
    tour = models.ForeignKey(Tour, null=True)
    final_cost = models.PositiveIntegerField(default=0)
    visibility = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.tour:
            self.final_cost = self.tour.price * self.amount_of_people
        super(Booking, self).save(*args, **kwargs)

    def price(self):
        cs = self.amount_of_people * self.tour.price
        return cs

    def __str__(self):
        return u'{}, ({:%d-%m-%Y} - {:%d-%m-%Y}), {}, {}'.format(self.status, self.start_date, self.fin_date,
                                                                 self.consumer,
                                                                 self.tour.name)


class Buying(models.Model):
    status = models.ForeignKey(Status, null=True)
    buy_date = models.DateTimeField(default=datetime.now, blank=True)
    amount_of_people = models.PositiveIntegerField(default=1)
    consumer = models.ForeignKey(User, null=True)
    tour = models.ForeignKey(Tour, null=True)
    final_cost = models.PositiveIntegerField(default=0)

    visibility = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.tour:
            self.final_cost = self.tour.price * self.amount_of_people
            # self.consumer = User.objects.get(user_)
        super(Buying, self).save(*args, **kwargs)

    def price(self):
        cs = self.amount_of_people * self.tour.price
        return cs

    def __str__(self):
        return u'{}, ({:%d-%m-%Y}), {} руб, {}, {}'.format(self.status, self.buy_date, self.final_cost, self.consumer,
                                                           self.tour.name)


class BuyTour(ModelForm):
    tag = models.IntegerField()

    class Meta:
        model = Buying
        exclude = ['visibility', 'final_cost', 'buy_date', 'status']
        # fields='__all__'
        # exclude = ['visibility', 'final_cost', 'buy_date']
        # Buying.status = Status.objects.get(name='запрос на бронь')


class BookTour(ModelForm):
    tag = models.IntegerField()

    class Meta:
        model = Booking
        exclude = ['visibility', 'start_date', 'fin_date', 'status', 'final_cost']
