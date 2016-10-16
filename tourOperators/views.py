from django.views.generic import ListView
from tourOperators.models import TourOperator
from tours.models import Tour
from tourOperators.models import AddTourForm
from django.http import HttpResponseRedirect


class TourOperListView(ListView):
    model = TourOperator


def add_tour(request):
    if request.method == 'POST':
        form = AddTourForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        start_date = form.cleaned_data['start_date']
        fin_date = form.cleaned_data['fin_date']
        tour = Tour.objects.create(
            name = name,
            price = price,
            start_date = start_date,
            fin_date = fin_date,
        )
        tour.save()
        return HttpResponseRedirect('/')
