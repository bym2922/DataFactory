from django.db import models
import time

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    # icon = models.ImageField(default='./factory/static/img/avatar-1.jpg')
    dept = models.CharField(max_length=128)
    job = models.CharField(max_length=128)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=64)
    power = models.IntegerField(default=1)
    date = models.DateField(default=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
