from django.views.generic import ListView
from tourOperators.models import TourOperator


class TourOperListView(ListView):
    model = TourOperator


