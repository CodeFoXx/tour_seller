import uuid

from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from datetime import datetime, timedelta, time
from django.utils import timezone

from consumers.models import Booking
from consumers.models import Buying
from consumers.models import Status
from tours.models import Tour
from django.shortcuts import render, redirect, get_object_or_404
import datetime


class BookingListView(ListView):
    model = Booking


class ByuingListView(ListView):
    model = Buying


class StatusListView(ListView):
    model = Status


@login_required
def book_tour(request, cur_id, amount, price):
    current_user = request.user
    book = Booking.objects.create(amount_of_people=amount, consumer=current_user)
    book.status = Status.objects.get(status='заявлен на бронь')
    book.tour_id = cur_id
    book.final_cost = int(amount) * int(price)
    book.save()
    return redirect('minus_tour', cur_id)


@login_required
def minus_tour(request, cur_id):
    tour = get_object_or_404(Tour, id=cur_id)
    tour.capacity -= 1
    tour.save()
    return redirect('tour_list_logon')


# @login_required
# def delete_book(request, cur_id):
#     book = get_object_or_404(Booking, id=cur_id)
#     if book.status ==
#     tour.capacity -= 1
#     tour.save()
#     return redirect('tour_list_logon')

@login_required
def cart(request):
    tim = (timezone.now() + timedelta(hours=7))
    current_user = request.user
    bookings = Booking.objects.filter(consumer=current_user).order_by('start_date')
    for book in bookings:
        print(book.fin_date)
        # if book.fin_date <= tim:
        #     b = get_object_or_404(Booking, id=book.id)
        #     b = Booking.objects.get(id=book.id)
        #     b.status = get_object_or_404(Booking, status='время бронирования истекло')
    return render(request, 'consumers/cart.html', dict(bookings=bookings))


@login_required
def buy_cart(request):
    current_user = request.user
    status = Status.objects.get(status='куплен')
    buyings = Buying.objects.filter(consumer=current_user, status=status).order_by('buy_date')
    return render(request, 'consumers/buy_cart.html', dict(buyings=buyings))


@login_required
def cancel_booking(request, cur_id):
    book = get_object_or_404(Booking, id=cur_id)
    book.status = Status.objects.get(status='бронь отклонена')
    book.tour.capacity += book.amount_of_people
    book.save()
    return redirect('touroperator_booking')


@login_required
def confirm_booking(request, cur_id):
    cur_booking = get_object_or_404(Booking, id=cur_id)
    cur_booking.status = Status.objects.get(status='бронь подтверждена')
    buying_status = Status.objects.get(status='куплен')
    new_buying = Buying(status=buying_status, buy_date=datetime.datetime.now(), amount_of_people=cur_booking.amount_of_people,
                        consumer=cur_booking.consumer, tour=cur_booking.tour, final_cost=cur_booking.final_cost)
    cur_booking.save()
    new_buying.save()
    return redirect('touroperator_booking')


@login_required
def touroperator_booking(request):
    current_user = request.user
    current_status = Status.objects.get(status='заявлен на бронь')
    bookings = Booking.objects.filter(tour__tour_operator=current_user).filter(status=current_status).order_by('start_date')
    return render(request, 'consumers/touroperator_booking.html', {'bookings': bookings})
