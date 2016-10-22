from django.views.generic import ListView
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf

from tours.models import Tour
from tours.models import AddTourForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.template import Context, loader
from django.http import HttpResponse


class TourListView(ListView):
    model = Tour


def tour_list_logon(request):
    tour_list_logon = Tour.objects.all()
    template = loader.get_template('tours/tour_list_logon.html')
    context = Context({
        'tour_list_logon': tour_list_logon,
    })
    return HttpResponse(template.render(context))

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
    del_tour = Tour.objects.filter(id=cur_id).delete()
    return redirect('touroperator_tour')
    #return render(request, 'tours/touroperator_tour.html', {'delete_tour': del_tour})
    #return render(request, 'tour_seller/touroperator_tour.html', {'delete_tour': del_tour})
