from django.views.generic import ListView

from consumers.models import Consumer
from consumers.models import Booking

class ConsumerListView(ListView):
    model = Consumer


class BookingListView(ListView):
    model = Booking
