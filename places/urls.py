from django.conf.urls import url

from places.views import CityListView
from places.views import CountryListView
from places.views import HotelListView

urlpatterns = [
    url('^$', CityListView.as_view(), name='city_list'),
    url('^$', CountryListView.as_view(), name='country_list'),
    url('^$', HotelListView.as_view(), name='hotel_list'),
]
