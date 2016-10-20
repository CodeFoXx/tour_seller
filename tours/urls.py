from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tours.views import add_tour
from tours.views import touroperator_tour
from tours.views import TourListView
from . import views

urlpatterns = [
    url('^details$', TourListView.as_view(template_name='tour_list'), name='tour_list'),
    #url('^$', TourListView.as_view(), name='tour_list'),
    url('^$', add_tour, name='add_tour'),
    url('^touroperator_tour$', views.touroperator_tour, name='touroperator_tour'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
