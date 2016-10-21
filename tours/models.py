from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.contrib import admin


from airlines.models import Airline
from places.models import Hotel
from places.models import City
from django.forms import ModelForm
# from consumers.models import Booking

from tour_seller.settings import MEDIA_ROOT
import os

class Tour(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    fin_date = models.DateTimeField()
    airline = models.ForeignKey(Airline)
    tour_operator = models.ForeignKey(User)
    capacity = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel)
    departure_city = models.ForeignKey(City)
    image = models.ImageField(blank=True,
                              upload_to = os.path.join('images', 'tours'), #'/images/tours/',
                              help_text='150x150px',
                              verbose_name='Изображение тура')
    visibility = models.BooleanField(default=True)


    def __str__(self):
        return '{} ({:%d-%m-%Y} - {:%d-%m-%Y})'.format(
            self.name, self.start_date, self.fin_date)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



class AddTourForm(ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'
        #exclude = ['title']






