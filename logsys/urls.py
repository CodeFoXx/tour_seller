from django.conf.urls import url,include
from logsys.views import register

urlpatterns = [
    url('^$', register),
]
