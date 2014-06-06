from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Balance(models.Model):
    pass


class Transaction(models.Model):
    pass


class Account(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username