from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=12)

    REQUIRED_FIELDS = ['name', 'phone_number']


class Room(models.Model):
    name = models.CharField(max_length=50)
    participants = models.ManyToManyField(User, related_name='rooms')
    phone_numbers = models.CharField(max_length=5000)
