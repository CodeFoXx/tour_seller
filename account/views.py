from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from datetime import datetime, timedelta, time
from django.utils import timezone
from consumers.models import Booking, Status
from tours.models import Tour
from account.models import UserProfile
from django.contrib import messages


def is_touroperator(user):
    return user.groups.filter(name='touroperator').exists()


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    newuser_form = UserCreationForm(request.POST)
    newuser_form.fields['username'].widget.attrs.update(
        {
            'placeholder': 'name@example.com'
        }
    )
    newuser_form.fields['password1'].widget.attrs.update(
        {
            'placeholder': 'password'
        }
    )
    newuser_form.fields['password2'].widget.attrs.update(
        {
            'placeholder': 'password'
        }
    )
    if newuser_form.is_valid():
        user = User.objects.create_user(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'],
                                        email=newuser_form.cleaned_data['username'])
        profile = UserProfile(user=user)
        profile.save()
        user.save()
        return HttpResponseRedirect('/')
    else:
        args['form'] = newuser_form
        return render_to_response('account/register.html', args)


def logon(request):
    c = {}
    c.update(csrf(request))
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            login(request, auth_user)
            current_user = request.user
            bookings = Booking.objects.filter(consumer=current_user).order_by('start_date')
            for book in bookings:
                tim = (timezone.now())
                # + timedelta(hours=7)
                current_user = request.user
                bookings = Booking.objects.filter(consumer=current_user).order_by('start_date')
                if book.fin_date <= tim:
                    print(book.tour_id)
                    if book.status.status == 'заявлен на бронь':
                        b = get_object_or_404(Booking, id=book.id)
                        status = Status.objects.get(status='время бронирования истекло')
                        b.status = status
                        b.save()
                        tour = get_object_or_404(Tour, id=book.tour_id)
                        tour.capacity += 1
                        tour.visibility = True
                        tour.save()
            if is_touroperator(auth_user):
                return redirect('/account/touroperator_dashboard')
            else:
                return redirect('/account/consumer_dashboard')
        else:
            messages.error(request, 'Неверный логин или пароль.')
            return render(request, 'account/logon.html', c)
    else:
        return render(request, 'account/logon.html', c)


def logout_user(request):
    logout(request)
    return render(request, 'tour_seller/index.html', {})


def add_inf_consumer(request):
    user = User.objects.get(username=request.user.username)
    c = {}
    c.update(csrf(request))
    if request.method == "POST":
        telephone = request.POST['tel']
        name = request.POST['first_name']
        second_name = request.POST['last_name']
        email = request.POST['email']
        user.userprofile.telephone = telephone
        user.userprofile.save()
        user.first_name = name
        user.last_name = second_name
        user.username = email
        user.email = email
        user.save()
        return redirect('/account/consumer_dashboard')
    else:
        return render(request, 'account/consumer_dashboard.html', c)


def add_inf_touroperator(request):
    user = User.objects.get(username=request.user.username)
    c = {}
    c.update(csrf(request))
    if request.method == "POST":
        telephone = request.POST['tel']
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            email = False
        user.userprofile.telephone = telephone
        user.userprofile.save()
        user.username = email
        user.email = email
        user.save()
        return redirect('/account/touroperator_dashboard')
    else:
        return render(request, 'account/touroperator_dashboard.html', c)
