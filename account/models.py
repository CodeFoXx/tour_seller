from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    telephone = models.CharField(max_length=11)
