from django.contrib import admin

from consumers.models import Consumer
from consumers.models import Booking
from consumers.models import Buying
from consumers.models import Status

admin.site.register(Consumer)
admin.site.register(Booking)
admin.site.register(Buying)
admin.site.register(Status)