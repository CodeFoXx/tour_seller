from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf

from tours.models import Tour


class TourListView(ListView):
    model = Tour


def BuyTour(request):
    args =  {}

#def BookTour(request):