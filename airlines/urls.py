from django.conf.urls import url

from airlines.views import AirlineListView

urlpatterns = [
    url('^$', AirlineListView.as_view(), name='airline_list')
]
