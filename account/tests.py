from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail
from django.test.client import Client

from account.models import UserProfile


class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("scat@mail.ru", "scat@mail.ru", "scat@mail.ru")
        profile = UserProfile(user=self.user)
        profile.save()
        self.user.save()
        # User.objects.create(name="cat", sound="meow")

    def test_user(self):
        """Users are correctly identified"""
        self.client.login(username="scat@mail.ru", password="scat@mail.ru")
        response = self.client.get('/account/consumer_dashboard')
        self.assertEqual(response.status_code, 200)
        params = {'first_name': 'Cat', 'last_name': 'Catalis', 'email': 'catalis@mail.ru', 'tel': '+79234456784'}
        response = self.client.post('/account/consumer_dashboard', params)
        self.assertEqual(response.status_code, 302)
        # post = Post.objects.get(title=params['first_name'])
