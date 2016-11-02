from django.test import TestCase

from django.contrib.auth.models import User, Group

from account.models import UserProfile
from consumers.models import Booking
from tours.models import Tour
from places.models import Country
from places.models import City
from places.models import Hotel
from airlines.models import Airline
from tours.views import touroperator_tour


class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="teztour@mail.ru", password="123123nn")
        g = Group.objects.create(name='touroperator')
        g.user_set.add(self.user)
        g.save()
        profile = UserProfile(user=self.user)
        profile.save()
        self.user.save()
        self.country = Country('UK')
        self.city = City(name='London', country=self.country)
        self.hotel = Hotel(city=self.city, stars='5')
        self.airline = Airline('British airways')
        self.new_tour = Tour(name='Christmas', price='1000',
                             start_date='20.12.2016', fin_date='10.01.2017',
                             airline=self.airline, tour_operator=self.user,
                             capacity='12', hotel=self.hotel,
                             departure_city=self.city, visibility=True)

    def testAdding(self):
        response1 = self.client.get('/account/logon')
        self.assertEqual(response1.status_code, 200)
        params1 = {'username': 'teztour@mail.ru', 'password': '123123nn'}
        response2 = self.client.post('/account/logon', params1)
        self.assertEqual(response2.status_code, 302)
        response3 = self.client.get('/tours/add_tour')
        self.assertEqual(response3.status_code, 200)
        params2 = {'name': 'Christmas tour', 'price': '100000', 'start_date': '20.12.2016', 'fin_date': '10.01.2017',
                   'capacity': '12', 'airline': self.airline, 'hotel': self.hotel, 'departure_city': self.city}
        response4 = self.client.post('/tours/add_tour', params2)
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(self.new_tour.tour_operator_id, self.user.id)
        request = self.client.get('/tours/touroperator_tour')
        request.user = self.user
        response = touroperator_tour(request)
        self.assertEqual(response.status_code, 200)
