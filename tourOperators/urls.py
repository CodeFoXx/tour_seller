from django.conf.urls import url
from tourOperators.views import TourOperListView

urlpatterns = [
    url('^$', TourOperListView.as_view(), name='tourOp_list'),
    ]
