from django.conf.urls import url

from tours.views import TourListView

urlpatterns = [
    url('^$', TourListView.as_view(), name='tour_list')
]
