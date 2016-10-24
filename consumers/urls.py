from django.conf.urls import url

from consumers.views import BookingListView
from consumers.views import ByuingListView
from consumers.views import StatusListView
from consumers.views import book_tour, buy_tour, b_tour, bo_tour

urlpatterns = [
    url('^book_tour$', book_tour, name='book_tour'),
    url('^buy_tour$', buy_tour, name='buy_tour'),
    url(r'^b_tour/(?P<cur_id>\d+)/(?P<amount>\d+)/(?P<status>\d+)/(?P<consumer>\d+)/$', b_tour, name='b_tour'),
    url(r'^bo_tour/(?P<cur_id>\d+)/(?P<amount>\d+)/(?P<status>\d+)/(?P<consumer>\d+)/$', bo_tour, name='bo_tour'),
]
