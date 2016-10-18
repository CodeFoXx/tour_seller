from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return u'{0},{1}'.format(self.country, self.name)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City)
    stars = models.SmallIntegerField(
        validators=(MinValueValidator(1),MaxValueValidator(5))
    )

    def __str__(self):
        return u'{},{},({} stars)'.format(self.city,self.name,self.stars)


