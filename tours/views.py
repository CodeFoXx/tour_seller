from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from tours.models import Tour
from tours.models import AddTourForm, ChangeTourForm
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.contrib.staticfiles.templatetags.staticfiles import static


class TourListView(ListView):
    model = Tour


@login_required
def add_tour(request):
    if request.method == 'POST':
        form = AddTourForm(request.POST, request.FILES)
        if form.is_valid():
            t_img = static('noimage.png')
            if form.cleaned_data['image']:
                t_img = form.cleaned_data['image']
            new_tour = Tour(name=form.cleaned_data['name'], price=form.cleaned_data['price'],
                            start_date=form.cleaned_data['start_date'], fin_date=form.cleaned_data['fin_date'],
                            airline=form.cleaned_data['airline'], tour_operator=form.cleaned_data['tour_operator'],
                            capacity=form.cleaned_data['capacity'], hotel=form.cleaned_data['hotel'],
                            departure_city=form.cleaned_data['departure_city'],
                            image=t_img, visibility=True)
            new_tour.save()
            return redirect('touroperator_tour')
        else:
            return TemplateResponse(request, 'tours/add_tour.html', dict(form=form))
    else:
        form = AddTourForm({'tour_operator': request.user})
        return TemplateResponse(request, 'tours/add_tour.html', dict(form=form))


@login_required
def touroperator_tour(request):
    current_user = request.user
    tours = Tour.objects.filter(tour_operator=current_user).order_by('price')
    return render(request, 'tours/touroperator_tour.html', {'tours': tours})


@login_required
def consumer_tour(request):
    tours = Tour.objects.all().order_by('price').filter(visibility=True)
    tim = (timezone.now())
    for tour in Tour.objects.all().filter(visibility=True):
        if tour.start_date <= tim:
            # print(tours.start_date)
            tour.visibility = False
            tour.save()
    return render(request, 'tours/consumer_tour.html', {'tours': tours})


@login_required
def delete_tour(request, cur_id):
    tour = get_object_or_404(Tour, id=cur_id)
    tour.visibility = False
    tour.save()
    return redirect('touroperator_tour')


@login_required
def change_tour(request, cur_id):
    if request.method == 'POST':
        form = ChangeTourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = get_object_or_404(Tour, id=cur_id)
            tour.name = form.cleaned_data['name']
            if form.cleaned_data['image']:
                tour.image = form.cleaned_data['image']
            tour.capacity = form.cleaned_data['capacity']
            tour.save()
        return redirect('touroperator_tour')
    else:
        request.session['session_tour_id'] = cur_id
        cur_tour = get_object_or_404(Tour, id=cur_id)
        form = ChangeTourForm({'name': cur_tour.name, 'image': cur_tour.image, 'capacity': cur_tour.capacity})
        return TemplateResponse(request, 'tours/change_tour.html', dict(form=form))
