from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib.auth import authenticate


def index(request):
    return render_to_response('tour_seller/index.html')


def logon(request):
    c = {}
    c.update(csrf(request))
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        seo_specialist = authenticate(username=username, password=password)
        if seo_specialist is not None:
            #если вошел перенаправляет на главную страницу
            return HttpResponseRedirect('/')
        else:
            # если не вошел
            return render_to_response('tour_seller/error_logon.html',c)
    else:
        # если POST запрос не был отправлен
        return render_to_response('tour_seller/logon.html', c)
