from django.conf.urls import url,include
from account.views import register, logon, logout_user, add_inf_consumer, add_inf_touroperator

urlpatterns = [
    url('^register$', register, name='register'),
    url('^logon$', logon,name='logon'),
    url('^logout_user$', logout_user, name='logout_user'),
    url('^consumer_dashboard$', add_inf_consumer, name='consumer_dashboard'),
    url('^touroperator_dashboard$', add_inf_touroperator, name='touroperator_dashboard')
]
