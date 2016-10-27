from django.conf.urls import url

from consumers.views import change_buy_status_cancel
from consumers.views import change_buy_status_confirm
from consumers.views import change_book_status_confirm
from consumers.views import change_book_status_cancel
from consumers.views import cart, buy_cart, request_from_consumer


urlpatterns = [
    # url(r'^book_tour$', book_tour, name='book_tour'),
    # url(r'^buy_tour$', buy_tour, name='buy_tour'),
    url('^cart', cart, name='cart'),
    url('^buy_cart', buy_cart, name='buy_cart'),
    url('^request_from_consumer', request_from_consumer, name='request_from_consumer'),
    url(r'^change_book_status_cancel/(?P<cur_id>\d+)/$', change_book_status_cancel, name='change_book_status_cancel'),
    url(r'^change_book_status_confirm/(?P<cur_id>\d+)/$', change_book_status_confirm, name='change_book_status_confirm'),
    url(r'^change_buy_status_cancel/(?P<cur_id>\d+)/$', change_buy_status_cancel, name='change_buy_status_cancel'),
    url(r'^change_buy_status_confirm/(?P<cur_id>\d+)/$', change_buy_status_confirm, name='change_buy_status_confirm'),

    # url(r'^b_tour/(?P<cur_id>\d+)/(?P<amount>\d+)/(?P<status>\d+)/(?P<consumer>\d+)/$', b_tour, name='b_tour'),
    # url(r'^bo_tour/(?P<cur_id>\d+)/(?P<amount>\d+)/(?P<status>\d+)/(?P<consumer>\d+)/$', bo_tour, name='bo_tour'),
]
