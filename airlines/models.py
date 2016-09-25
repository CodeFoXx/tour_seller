from django.db import models


class Airline(models.Model):
    NameAir = models.CharField(max_length=50)
