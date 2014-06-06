from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=60)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=128)
    time_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    body = models.TextField()
    image = models.ImageField(upload_to='blog/post_images', blank=True)


class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    anonymous = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=30)
    body = models.TextField()
