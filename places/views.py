from django.views.generic import ListView

from places.models import City
from places.models import Country
from places.models import Hotel


class CityListView(ListView):
    model = City


class CountryListView(ListView):
    model = Country


class HotelListView(ListView):
    model = Hotel
