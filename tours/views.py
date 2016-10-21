from django.views.generic import ListView
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf

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
        form = AddTourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return TemplateResponse(request, 'tours/add_tour.html', dict(form=form))
    else:
        form = AddTourForm()
        return TemplateResponse(request, 'tours/add_tour.html', dict(form=form))


@login_required
def touroperator_tour(request):
    current_user = request.user
    tours = Tour.objects.filter(tour_operator=current_user).order_by('price')
    return render(request, 'tours/touroperator_tour.html', {'tours': tours})


@login_required
def delete_tour(request, cur_id):
    tour = Tour.objects.filter(id=cur_id).get()
    tour.visibility = False
    tour.save()
    return redirect('touroperator_tour')