from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render_to_response('tour_seller/index.html')


def logon(request):
    c = {}
    c.update(csrf(request))
    newuser_form=AuthenticationForm
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        seo_specialist = authenticate(username=username, password=password)
        if seo_specialist is not None:
            if seo_specialist.is_active:
                return HttpResponseRedirect('/')
            else:
            # если не вошел
                c['form'] = newuser_form
                return render_to_response('tour_seller/error_logon.html',c)
        else:
        # если POST запрос не был отправлен
            c['form'] = newuser_form
            return render_to_response('tour_seller/error_logon.html', c)

    else:
        # если POST запрос не был отправлен
        c['form'] = newuser_form
        return render_to_response('tour_seller/logon.html', c)