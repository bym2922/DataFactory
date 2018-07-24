from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=64)
    power = models.IntegerField(default=1)
