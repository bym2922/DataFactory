from django.db import models
from user.models import User
# Create your models here.


class File(models.Model):
    fname = models.CharField(max_length=128, unique=True)
    date = models.CharField(max_length=128)
    fpath = models.CharField(max_length=256)
    uname = models.CharField(max_length=128)

    @property
    def auth(self):
        if not hasattr(self, '_auth'):
            self._user = User.objects.get(id=self.uid)
        return self._user

