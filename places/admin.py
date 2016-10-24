from django.contrib import admin

from places.models import City
from places.models import Country
from places.models import Hotel

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Hotel)
