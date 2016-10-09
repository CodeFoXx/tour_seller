from django.views.generic import ListView

from touroperators.models import TourOperator


class TourOperListView(ListView):
    model = TourOperator
