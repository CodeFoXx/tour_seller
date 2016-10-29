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


class BookingListView(ListView):
    model = Booking


class ByuingListView(ListView):
    model = Buying


class StatusListView(ListView):
    model = Status


@login_required
def tour_list_logon(request):
    tours = Tour.objects.all()
    return render(request, 'tours/tour_list_logon.html', {'tours': tours})


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
def buy_tour(request, cur_id, amount, price):
    current_user = request.user
    buy = Buying.objects.create(amount_of_people=amount, consumer=current_user)
    buy.status = Status.objects.get(status='заявлен на покупку')
    buy.tour_id = cur_id
    buy.final_cost = int(amount) * int(price)
    buy.save()
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
    status = Status.objects.get(status='покупка подтверждена')
    buyings = Buying.objects.filter(consumer=current_user, status=status).order_by('buy_date')
    return render(request, 'consumers/buy_cart.html', dict(buyings=buyings))


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
