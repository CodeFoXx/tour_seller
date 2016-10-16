from django.db import models
from django.forms import ModelForm
from tours.models import Tour


class TourOperator(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=11, default="")

    def __str__(self):
        return u'{}, {}, {}'.format(self.name, self.email, self.phone)


class AddTourForm(ModelForm):
    class Meta:
        model = Tour, TourOperator
        fields = '__all__'
        #exclude = ['title']
