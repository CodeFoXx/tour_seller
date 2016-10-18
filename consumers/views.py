from django.views.generic import ListView

from consumers.models import Booking


class BookingListView(ListView):
    model = Booking
