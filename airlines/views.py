from django.views.generic import ListView

from airlines.models import Airline


class AirlineListView(ListView):
    model = Airline
