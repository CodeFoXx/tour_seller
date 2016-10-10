from django.shortcuts import render_to_response
from django.contrib import auth


def index(request):

   return render_to_response('tour_seller/index.html')


