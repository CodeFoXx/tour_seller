from django.conf.urls import url

from consumers.views import BookingListView
from consumers.views import ByuingListView
from consumers.views import StatusListView
from consumers.views import book_tour
from consumers.views import buy_tour

urlpatterns = [
    url('^book_tour$', book_tour, name='book_tour'),
    url('^buy_tour$', buy_tour, name='buy_tour'),
    url('^$', BookingListView.as_view(), name='booking_list'),
    url('^$', ByuingListView.as_view(), name='buying_list'),
    url('^$', StatusListView.as_view(), name='status_list'),
]
