from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    newuser_form = UserCreationForm(request.POST)
    newuser_form.fields['username'].widget.attrs.update(
        {
            'placeholder':'name@example.com'
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
        user = User.objects.create_user(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
        user.save()
        return HttpResponseRedirect('/')
    else:
        args['form'] = newuser_form
        return render_to_response('logsys/register.html', args)
