from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.template import RequestContext
from django.template.context_processors import csrf
# Create your views here.
from consumers.models import Consumer


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()

    newuser_form = UserCreationForm(request.POST)

    if newuser_form.is_valid():
        user = User.objects.create_user(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
        user.is_active = False
        user.save()
        return HttpResponseRedirect('/')
    else:
        args['form'] = newuser_form
        return render_to_response('reg/reg.html', args)
