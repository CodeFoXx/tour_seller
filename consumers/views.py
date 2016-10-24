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
from django.shortcuts import render, redirect, render_to_response


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
            return render_to_response(request, 'tours/buy_tour.html', dict(form=form))
    else:
        form = BuyTour({'consumer': request.user})
        return render_to_response(request, 'tours/buy_tour.html', dict(form=form))


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


@login_required
def b_tour(request, cur_id, amount, status, consumer):
    tour1 = Tour.objects.filter(id=cur_id).get()
    status = Status.objects.filter(id=1).get()
    buy_t = Buying(tour=tour1.objects.get(id), amount_of_people=amount, status=status,
                   consumer=consumer, visibility=True)
    buy_t.save()
    return HttpResponseRedirect('/')


@login_required
def bo_tour(request, cur_id, amount, status, consumer):
    tour1 = Tour.objects.filter(id=cur_id).get()
    status = Status.objects.filter(id=1).get()
    book_t = Buying(tour=tour1.objects.get(id), amount_of_people=amount, status=status,
                    consumer=consumer, visibility=True)
    book_t.save()
    return HttpResponseRedirect('/')
