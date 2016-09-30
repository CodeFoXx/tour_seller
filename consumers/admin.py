from django.contrib import admin

from consumers.models import Consumer
from consumers.models import Booking

admin.site.register(Consumer)
admin.site.register(Booking)