from django.shortcuts import get_object_or_404
from django_cron import CronJobBase, Schedule
from consumers.models import Booking
from datetime import datetime, timedelta, time
from django.utils import timezone


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tour_seller.my_cron_job'  # a unique code

    def do(self):
        tim = (timezone.now() + timedelta(hours=7))
        for book in Booking.objects.all():
            print(book.fin_date)
            if book.fin_date <= tim:
                print(book.fin_date)
                print(tim)
                b = get_object_or_404(Booking, id=book.id)
                b = Booking.objects.get(id=book.id)
                b.delete()
