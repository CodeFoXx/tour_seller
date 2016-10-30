from django.conf.urls import url

from consumers.views import consumer_booking_cart, consumer_buying_cart, touroperator_booking, cancel_booking,\
    confirm_booking, touroperator_buying_history, delete_booking


urlpatterns = [
    url('^consumer_booking_cart', consumer_booking_cart, name='consumer_booking_cart'),
    url('^consumer_buying_cart', consumer_buying_cart, name='consumer_buying_cart'),
    url(r'^cancel_booking/(?P<cur_id>\d+)/$', cancel_booking, name='cancel_booking'),
    url(r'^delete_booking/(?P<cur_id>\d+)/$', delete_booking, name='delete_booking'),
    url(r'^confirm_booking/(?P<cur_id>\d+)/$', confirm_booking, name='confirm_booking'),
    url('^touroperator_booking', touroperator_booking, name='touroperator_booking'),
    url('^touroperator_buying_history', touroperator_buying_history, name='touroperator_buying_history'),


]
