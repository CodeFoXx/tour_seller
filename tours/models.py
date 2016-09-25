from django.db import models

from airlines.models import Airline
from tourOperators.models import TourOperator
from places.models import Hotel
from places.models import City


class Tour(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    StartDate = models.DateField()
    FinDate = models.DateField()
    airline = models.ForeignKey(Airline)
    tourOperator = models.ForeignKey(TourOperator)
    capacity = models.PositiveIntegerField()
    destination = models.ForeignKey(Hotel)
    departureCity = models.ForeignKey(City)




