from django.test import TestCase
from django.contrib.auth.models import User, Group
from account.models import UserProfile
from consumers.models import Status
from consumers.views import book_tour, minus_tour
from tours.models import Tour
from places.models import Country
from places.models import City
from places.models import Hotel
from airlines.models import Airline
from tours.views import touroperator_tour, delete_tour, consumer_tour


class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="teztour@mail.ru", password="123123nn")
        g = Group.objects.create(name='touroperator')
        g.user_set.add(self.user)
        g.save()
        profile = UserProfile(user=self.user)
        profile.save()
        self.user.save()
        self.country = Country('2')
        self.country.save()
        self.city = City(name='London', country=self.country)
        self.city.save()
        self.hotel = Hotel(city=self.city, stars='5')
        self.hotel.save()
        self.airline = Airline(2)
        self.airline.save()
        self.new_tour = Tour(name='Christmas', price='100',
                             start_date='2016-12-20 23:20', fin_date='2017-01-10 20:12',
                             airline=self.airline, tour_operator=self.user,
                             capacity='12', hotel=self.hotel,
                             departure_city=self.city, image='3190-5.jpg', visibility=True)
        self.new_tour.save()
        Status.objects.create(status='заявлен на бронь')
        Status.objects.create(status='куплен')
        Status.objects.create(status='бронь отклонена')

    def test_tour(self):
        response1 = self.client.get('/account/logon')
        self.assertEqual(response1.status_code, 200)
        params1 = {'username': 'teztour@mail.ru', 'password': '123123nn'}
        response2 = self.client.post('/account/logon', params1)
        self.assertEqual(response2.status_code, 302)
        response3 = self.client.get('/tours/add_tour')
        self.assertEqual(response1.status_code, 200)
        params = {'name': 'Рождество', 'price': '100000', 'start_date': '2016-12-20 23:20',
                  'fin_date': '2017-01-10 20:12', 'capacity': '15', 'airline': self.airline.id,
                  'tour_operator': self.new_tour.tour_operator_id,
                  'hotel': self.hotel.id, 'departure_city': self.city.id,
                  'image': self.new_tour.image}
        response = self.client.post('/tours/add_tour', params)
        self.assertEqual(response.status_code, 302)
        request = self.client.get('/tours/touroperator_tour')
        request.user = self.user
        response = touroperator_tour(request)
        self.assertEqual(response.status_code, 200)
        response4 = self.client.post('/tours/change_tour/1/')
        self.assertEqual(response4.status_code, 302)
        params2 = {'name': 'Рождество в Лондоне', 'capacity': '15'}
        response2 = self.client.post('/tours/change_tour/1/', params2)
        self.assertEqual(response2.status_code, 302)
        request = self.client.get('/tours/details')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('/tours/touroperator_tour')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('/consumers/touroperator_booking')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('/consumers/touroperator_buying_history')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('/account/logout_user')
        self.assertEqual(request.status_code, 200)

        self.user = User.objects.create_user(username="consumer2@mail.ru", password="123123nn",
                                             email="consumer2@mail.ru")
        profile = UserProfile(user=self.user)
        profile.save()
        self.user.save()
        response1 = self.client.get('/account/logon')
        self.assertEqual(response1.status_code, 200)
        params1 = {'username': 'consumer2@mail.ru', 'password': '123123nn'}
        response2 = self.client.post('/account/logon', params1)
        self.assertEqual(response2.status_code, 302)

        request = self.client.post('/tours/consumer_tour')
        self.assertEqual(response.status_code, 200)
        request.user = self.user
        response = book_tour(request, self.new_tour.id, 15, '100000')
        self.assertEqual(response.status_code, 302)
        response = minus_tour(request, self.new_tour.id)
        self.assertEqual(response.status_code, 302)

        request = self.client.get('/consumers/consumer_booking_cart')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('/consumers/consumer_buying_cart')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('/tours/consumer_tour')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('/tours/details')
        self.assertEqual(request.status_code, 200)
        request = self.client.get('/index')
        self.assertEqual(request.status_code, 200)


        request = self.client.get('/account/logout_user')
        self.assertEqual(request.status_code, 200)

        response1 = self.client.get('/account/logon')
        self.assertEqual(response1.status_code, 200)
        params1 = {'username': 'teztour@mail.ru', 'password': '123123nn'}
        response2 = self.client.post('/account/logon', params1)
        self.assertEqual(response2.status_code, 302)
        request = self.client.get('/tours/touroperator_tour')
        request.user = self.user
        response = delete_tour(request, self.new_tour.id)
        self.assertEqual(response.status_code, 302)




