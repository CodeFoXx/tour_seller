from django.conf.urls import url

from consumers.views import cart, buy_cart, touroperator_booking, cancel_booking, confirm_booking, \
    touroperator_buying_history, delete_book


urlpatterns = [
    url('^cart', cart, name='cart'),
    url('^buy_cart', buy_cart, name='buy_cart'),
    url(r'^cancel_booking/(?P<cur_id>\d+)/$', cancel_booking, name='cancel_booking'),
    url(r'^delete_book/(?P<cur_id>\d+)/$', delete_book, name='delete_book'),
    url(r'^confirm_booking/(?P<cur_id>\d+)/$', confirm_booking, name='confirm_booking'),
    url('^touroperator_booking', touroperator_booking, name='touroperator_booking'),
    url('^touroperator_buying_history', touroperator_buying_history, name='touroperator_buying_history'),


]
