from django.conf.urls import url

from consumers.views import change_buy_status_cancel
from consumers.views import change_buy_status_confirm
from consumers.views import change_book_status_confirm
from consumers.views import change_book_status_cancel
from consumers.views import cart, buy_cart, touroperator_booking


urlpatterns = [
    url('^cart', cart, name='cart'),
    url('^buy_cart', buy_cart, name='buy_cart'),
    url(r'^change_book_status_cancel/(?P<cur_id>\d+)/$', change_book_status_cancel, name='change_book_status_cancel'),
    url(r'^change_book_status_confirm/(?P<cur_id>\d+)/$', change_book_status_confirm, name='change_book_status_confirm'),
    url(r'^change_buy_status_cancel/(?P<cur_id>\d+)/$', change_buy_status_cancel, name='change_buy_status_cancel'),
    url(r'^change_buy_status_confirm/(?P<cur_id>\d+)/$', change_buy_status_confirm, name='change_buy_status_confirm'),
    url('^touroperator_booking', touroperator_booking, name='touroperator_booking'),


]
