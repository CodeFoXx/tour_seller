from django.shortcuts import render_to_response


def index(request):
   return render_to_response('tour_seller/index.html')


def logon(request):
   return render_to_response('tour_seller/logon.html')