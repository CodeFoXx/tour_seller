from django.views.generic import ListView
from tours.models import Tour
from tours.models import AddTourForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse


class TourListView(ListView):
    model = Tour


@login_required
def add_tour(request):
    if request.method == 'POST':
        form = AddTourForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return TemplateResponse(request, 'tours/add_tour.html', dict(form=form))
    else:
        form = AddTourForm()
        return TemplateResponse(request, 'tours/add_tour.html', dict(form=form))


