import uuid
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
from django.shortcuts import render, redirect



class BookingListView(ListView):
    model = Booking


class ByuingListView(ListView):
    model = Buying


class StatusListView(ListView):
    model = Status

@login_required
def buy_tour(request):
    if request.method == 'POST':
        form = BuyTour(request.POST)
        if form.is_valid():
            new_buy = Buying(amount_of_people=form.cleaned_data['amount_of_people'],
                             consumer=form.cleaned_data['consumer'],
                             # status=form.cleaned_data['status'],
                             tour=form.cleaned_data['tour'], visibility=True)
            new_buy.save()
            return HttpResponseRedirect('/')
        else:
            return TemplateResponse(request, 'tours/buy_tour.html', dict(form=form))
    else:
        form = BuyTour({'consumer': request.user})
        return TemplateResponse(request, 'tours/buy_tour.html', dict(form=form))


@login_required
def book_tour(request):
    if request.method == 'POST':
        form = BookTour(request.POST, request.FILES)
        if form.is_valid():
            new_book = Booking(amount_of_people=form.cleaned_data['amount_of_people'],
                             consumer=form.cleaned_data['consumer'],
                             # status=form.cleaned_data['status'],
                             tour=form.cleaned_data['tour'], visibility=True)
            new_book.save()
            return HttpResponseRedirect('/')
        else:
            return TemplateResponse(request, 'tours/book_tour.html', dict(form=form))
    else:
        form = BookTour({'consumer': request.user})
        return TemplateResponse(request, 'tours/book_tour.html', dict(form=form))


