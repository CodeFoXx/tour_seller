from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf

from account.models import UserProfile


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
            if is_touroperator(auth_user):
                return redirect('/account/touroperator_dashboard')
            else:
                return redirect('/account/consumer_dashboard')
        else:
            # если не вошел
            return render(request, 'account/error_logon.html', c)
    else:
        # если POST запрос не был отправлен
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
        email = request.POST['email']
        user.userprofile.telephone = telephone
        user.userprofile.save()
        user.username = email
        user.email = email
        user.save()
        return redirect('/account/touroperator_dashboard')
    else:
        return render(request, 'account/touroperator_dashboard.html', c)
