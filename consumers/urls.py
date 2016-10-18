from django.conf.urls import url

from consumers.views import BookingListView

urlpatterns = [
    url('^$', BookingListView.as_view(), name='booking_list'),
]
