from django.contrib.auth.models import User
from django.test import TestCase
from account.models import UserProfile
from django.contrib.auth.models import Group


class SimpleTest(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username="teztour@mail.ru", password="123123nn")
            g = Group.objects.create(name='touroperator')
            g.user_set.add(self.user)
            g.save()
            profile = UserProfile(user=self.user)
            profile.save()
            self.user.save()
            self.user = User.objects.create_user(username="mmcat@mail.ru", password="123123nn")
            profile = UserProfile(user=self.user)
            profile.save()
            self.user.save()

        def test_reg(self):
            response = self.client.get('/account/register')
            self.assertEqual(response.status_code, 200)
            params = {'username': 'nvk@mail.ru', 'password1': '123123nn', 'password2': '123123nn'}
            response = self.client.post('/account/register', params)
            self.assertEqual(response.status_code, 302)

        def test_tourperator(self):
            response = self.client.get('/account/logon')
            self.assertEqual(response.status_code, 200)
            params = {'username': 'teztour@mail.ru', 'password': '123123nn'}
            response = self.client.post('/account/logon', params)
            self.assertEqual(response.status_code, 302)
            response = self.client.get('/account/touroperator_dashboard')
            self.assertEqual(response.status_code, 200)
            params = {'tel': '+7800600500', 'email': 'teztour@mail.ru'}
            response = self.client.post('/account/touroperator_dashboard', params)
            self.assertEqual(response.status_code, 302)

        def test_valid_consumer(self):
            response1 = self.client.get('/account/logon')
            self.assertEqual(response1.status_code, 200)
            params = {'username': 'mmcat@mail.ru', 'password': '123123nn'}
            response2 = self.client.post('/account/logon', params)
            self.assertEqual(response2.status_code, 302)
            response3 = self.client.get('/account/consumer_dashboard')
            self.assertEqual(response3.status_code, 200)
            params = {'first_name': 'Cat', 'last_name': 'Catalis', 'email': 'catalis@mail.ru', 'tel': '+79234456784'}
            response4 = self.client.post('/account/consumer_dashboard', params)
            self.assertEqual(response4.status_code, 302)

        def test_invalid_consumer(self):
            response1 = self.client.get('/account/logon')
            self.assertEqual(response1.status_code, 200)
            params = {'username': 'mmcat@mail.ru', 'password': '1231nn'}
            response2 = self.client.post('/account/logon', params)
            self.assertEqual(response2.status_code, 200)
