from django.conf.urls import url

from touroperators.views import TourOperListView

urlpatterns = [
    url('^$', TourOperListView.as_view(), name='tourOp_list')
]
