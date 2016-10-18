from django.views.generic import ListView

from consumers.models import Booking
from consumers.models import Buying
from consumers.models import Status



class BookingListView(ListView):
    model = Booking


class ByuingListView(ListView):
    model = Buying


class StatusListView(ListView):
    model = Status
