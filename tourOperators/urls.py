from django.conf.urls import url
from tourOperators.views import TourOperListView
from tourOperators.views import add_tour

urlpatterns = [
    url('^$', TourOperListView.as_view(), name='tourOp_list'),
    url('^$', add_tour),
]
