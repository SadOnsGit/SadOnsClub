from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUsers(AbstractUser):
    bonuses = models.IntegerField(default=0)
    money = models.FloatField(default=0)