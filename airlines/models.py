from django.db import models


class Airline(models.Model):
    NameAir = models.CharField(max_length=50)

    def __str__(self):
        return self.NameAir
