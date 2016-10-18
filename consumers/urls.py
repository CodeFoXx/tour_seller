from django.conf.urls import url

from consumers.views import ConsumerListView
from consumers.views import BookingListView
from consumers.views import ByuingListView
from consumers.views import StatusListView

urlpatterns = [
    url('^$', ConsumerListView.as_view(), name='consumer_list'),
    url('^$', BookingListView.as_view(), name='booking_list'),
    url('^$', ByuingListView.as_view(), name='buying_list'),
    url('^$', StatusListView.as_view(), name='status_list'),
]
