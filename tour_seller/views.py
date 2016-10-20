from django.shortcuts import render_to_response, render


def index(request):
    return render(request, 'tour_seller/index.html', {})


def touroperator_dashboard(request):
    return render_to_response('tour_seller/../templates/tours/touroperator_dashboard.html')


def consumer_dashboard(request):
    return render_to_response('tour_seller/../templates/tours/consumer_dashboard.html')
