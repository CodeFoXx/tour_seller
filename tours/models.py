from django.db import models
from PIL import Image
from django.contrib import admin


from airlines.models import Airline
from tourOperators.models import TourOperator
from places.models import Hotel
from places.models import City
# from consumers.models import Booking


class Tour(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    fin_date = models.DateTimeField()
    airline = models.ForeignKey(Airline)
    tour_operator = models.ForeignKey(TourOperator)
    capacity = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel)
    departure_city = models.ForeignKey(City)
    image = models.ImageField(blank=True,
                              upload_to='images/tours/',
                              help_text='150x150px',
                              verbose_name='Изображение тура')
    # booking = models.ForeignKey(Booking)

    def __str__(self):
        return '{} ({:%d-%m-%Y} - {:%d-%m-%Y})'.format(
            self.name, self.start_date, self.fin_date)






