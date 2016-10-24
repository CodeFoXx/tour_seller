from django.conf.urls import url

from account.views import register, logon, logout_user

urlpatterns = [
    url('^register$', register, name='register'),
    url(r'^logon', logon, name='logon'),
    url(r'^logout_user', logout_user, name='logout_user'),
]
