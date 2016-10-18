from django.contrib.auth.models import User
from django.db import models
from tours.models import Tour



class Booking(models.Model):
    status = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    fin_date = models.DateTimeField()
    consumer = models.ForeignKey(User, null=True)
    tour = models.ForeignKey(Tour, null=True)

    def __str__(self):
        return u'{}, {}, {}, {}, {}'.format(self.status, self.start_date, self.fin_date, self.consumer,
                                            self.tour)
