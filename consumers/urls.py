from django.conf.urls import url

from consumers.views import ConsumerListView
from consumers.views import BookingListView

urlpatterns = [
    url('^$', ConsumerListView.as_view(), name='consumer_list'),
    url('^$', BookingListView.as_view(), name='booking_list'),
]
