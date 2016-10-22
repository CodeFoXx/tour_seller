from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from consumers.models import Booking
from consumers.models import Buying
from consumers.models import Status
from consumers.models import BuyTour
from consumers.models import BookTour
from tours.models import Tour
from django.http import HttpResponseRedirect



class BookingListView(ListView):
    model = Booking


class ByuingListView(ListView):
    model = Buying


class StatusListView(ListView):
    model = Status


@login_required
def buy_tour(request):
    user = User.objects.get(username=request.user.username)
    user.id
    if request.method == 'POST':
        form = BuyTour(request.POST, request.FILES)
        tour = Tour(request.POST)

        current_user = request.user
        if form.is_valid():
            # feedback = form.save(commit=False)
            # consumer = User.objects.get()
            #
            # feedback.save()
            consumer = user.id
            form.consumer = consumer
            form.save()
            return HttpResponseRedirect('/')
        else:
            return TemplateResponse(request, 'tours/buy_tour.html', dict(form=form))
    else:
        form = BuyTour()
        return TemplateResponse(request, 'tours/buy_tour.html', dict(form=form))


@login_required
def book_tour(request):
    if request.method == 'POST':
        form = BookTour(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return TemplateResponse(request, 'tours/tour_list_logon.html', dict(form=form))
    else:
        form = BookTour()
        return TemplateResponse(request, 'tours/tour_list_logon.html', dict(form=form))


