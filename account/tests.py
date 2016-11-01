from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from account.models import UserProfile
from django.contrib.auth.models import Group

class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("scat@mail.ru", "scat@mail.ru", "123123nn")
        profile = UserProfile(user=self.user)
        profile.save()
        self.user.save()

    def test_consumer(self):
        """Users are correctly comes to consumer_dashboard """
        self.client.login(username="scat@mail.ru", password="123123nn")
        response = self.client.get('/account/consumer_dashboard')
        self.assertEqual(response.status_code, 200)
        params = {'first_name': 'Cat', 'last_name': 'Catalis', 'email': 'catalis@mail.ru', 'tel': '+79234456784'}
        response = self.client.post('/account/consumer_dashboard', params)
        self.assertEqual(response.status_code, 302)

    def test_touroperator(self):
        """Users are correctly comes to touroperator_dashboard """
        self.user = User.objects.create_user(username="teztour@mail.ru", password="123123nn")
        g = Group.objects.create(name='touroperator')
        g.user_set.add(self.user)
        g.save()
        profile = UserProfile(user=self.user)
        profile.save()
        self.user.save()

        self.client.login(username="teztour@mail.ru",email="teztour@mail.ru", password="123123nn")
        response = self.client.get('/account/touroperator_dashboard')
        self.assertEqual(response.status_code, 200)
        params = {'tel': '+7800600500'}
        response = self.client.post('/account/touroperator_dashboard', params)
        self.assertEqual(response.status_code, 302)