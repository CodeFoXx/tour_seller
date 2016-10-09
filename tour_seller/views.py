from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):
   return render_to_response('tour_seller/index.html')


def register(request):
   return render_to_response('tour_seller/register.html')


def logon(request):
   return render_to_response('tour_seller/logon.html')