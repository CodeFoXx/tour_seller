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
from django.shortcuts import render, redirect, render_to_response, get_object_or_404


class BookingListView(ListView):
    model = Booking


class ByuingListView(ListView):
    model = Buying


class StatusListView(ListView):
    model = Status


@login_required
def buy_tour(request):
    if request.method == 'POST':
        form = BuyTour(data=request.POST or None)
        if form.is_valid():
            new_buy = Buying(amount_of_people=form.cleaned_data['amount_of_people'],
                             consumer=form.cleaned_data['consumer'],
                             # status=form.cleaned_data['status'],
                             tour=form.cleaned_data['tour'], visibility=True)
            new_buy.save()
            return HttpResponseRedirect('/')
        else:
            return TemplateResponse(request, 'tours/tour_list.html', dict(form=form))
    else:
        form = BuyTour({'consumer': request.user})
        return TemplateResponse(request, 'tours/tour_list.html', dict(form=form))


@login_required
def book_tour(request):
    if request.method == 'POST':
        form = BookTour(request.POST)
        if form.is_valid():
            new_book = Booking(amount_of_people=form.cleaned_data['amount_of_people'],
                               consumer=form.cleaned_data['consumer'],
                               # status=form.cleaned_data['status'],
                               tour=form.cleaned_data['tour'], visibility=True)
            new_book.save()
            return redirect('/')
        else:
            return TemplateResponse(request, 'tours/tour_list.html', dict(form=form))
    else:
        form = BookTour({'consumer': request.user})
        return TemplateResponse(request, 'tours/tour_list.html', dict(form=form))


# @login_required
# def b_tour(request, cur_id, amount, status, consumer):
#     tour1 = Tour.objects.filter(id=cur_id).get()
#     status = Status.objects.filter(id=1).get()
#     buy_t = Buying(tour=tour1.objects.get(id), amount_of_people=amount, status=status,
#                    consumer=consumer, visibility=True)
#     buy_t.save()
#     return HttpResponseRedirect('/')
#
#
# @login_required
# def bo_tour(request, cur_id, amount, status, consumer):
#     tour1 = Tour.objects.filter(id=cur_id).get()
#     status = Status.objects.filter(id=1).get()
#     book_t = Buying(tour=tour1.objects.get(id), amount_of_people=amount, status=status,
#                     consumer=consumer, visibility=True)
#     book_t.save()
#     return HttpResponseRedirect('/')

@login_required
def cart(request):
    current_user = request.user
    bookings = Booking.objects.filter(consumer=current_user).order_by('start_date')
    buyings = Buying.objects.filter(consumer=current_user).order_by('buy_date')
    return render(request, 'tours/cart.html', dict(bookings=bookings, buyings=buyings))


@login_required
def request_from_consumer(request):
    current_user = request.user
    tours = Tour.objects.get(tour_operator=current_user)
    bookings = Booking.objects.filter(tour=tours).order_by('start_date')
    buyings = Buying.objects.filter(tour=tours).order_by('buy_date')
    return render(request, 'tours/request_from_consumer.html', dict(bookings=bookings, buyings=buyings))


@login_required
def change_book_status_cancel(request, cur_id):
    book = get_object_or_404(Booking, id=cur_id)
    book.status = get_object_or_404(Booking, status='бронь отклонена')
    book.save()
    return redirect('request_from_consumer')


@login_required
def change_book_status_confirm(request, cur_id):
    book = get_object_or_404(Booking, id=cur_id)
    book.status = get_object_or_404(Booking, status='бронь подтверждена')
    book.save()
    return redirect('request_from_consumer')


@login_required
def change_buy_status_cancel(request, cur_id):
    buy = get_object_or_404(Buying, id=cur_id)
    buy.status = Status.objects.get(status='покупка отклонена')
    buy.save()
    return redirect('request_from_consumer')


@login_required
def change_buy_status_confirm(request, cur_id):
    buy = get_object_or_404(Buying, id=cur_id)
    buy.status = Status.objects.get(status='покупка подтверждена')
    buy.save()
    return redirect('request_from_consumer')
