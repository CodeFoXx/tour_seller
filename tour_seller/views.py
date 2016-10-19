from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'tour_seller/index.html', {})


def touroperator_dashboard(request):
    return render_to_response('tour_seller/touroperator_dashboard.html')


def consumer_dashboard(request):
    return render_to_response('tour_seller/consumer_dashboard.html')


def is_touroperator(user):
    return user.groups.filter(name='touroperator').exists()


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
                return render(request, 'tour_seller/touroperator_dashboard.html', c)
            else:
                return render(request, 'tour_seller/consumer_dashboard.html', c)
        else:
            # если не вошел
            return render(request, 'tour_seller/error_logon.html', c)
    else:
        # если POST запрос не был отправлен
        return render(request, 'tour_seller/logon.html', c)

def logout_user(request):
    logout(request)
    return render(request, 'tour_seller/index.html', {})
