from django.conf.urls import url

from tours.views import TourListView

urlpatterns = [
    url('^$', TourListView.as_view(), name='tour_list'),
    # url('^details$', TourListView.as_view(template_name=), name='tour_list'),
]
