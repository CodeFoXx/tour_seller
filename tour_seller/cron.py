from django.shortcuts import get_object_or_404
from django_cron import CronJobBase, Schedule
from consumers.models import Booking, Status
from tours.models import Tour
from datetime import datetime, timedelta, time
from django.utils import timezone


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # every 5 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tour_seller.my_cron_job'  # a unique code

    def do(self):
        for book in Booking.objects.all():
            tim = (timezone.now())
            # + timedelta(hours=7)
            if book.fin_date <= tim:
                print(book.tour_id)
                if book.status.status == 'заявлен на бронь':
                    b = get_object_or_404(Booking, id=book.id)
                    status = Status.objects.get(status='время бронирования истекло')
                    b.status = status
                    b.save()
                    tour = get_object_or_404(Tour, id=book.tour_id)
                    tour.capacity += 1
                    tour.visibility = True
                    tour.save()
