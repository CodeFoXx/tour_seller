from django.conf.urls import url

from consumers.views import BookingListView
from consumers.views import ByuingListView
from consumers.views import StatusListView
from consumers.views import book_tour
from consumers.views import buy_tour

urlpatterns = [
    url('^book_tour$', book_tour, name='book_tour'),
    url('^buy_tour$', buy_tour, name='buy_tour'),
]
