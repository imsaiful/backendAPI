from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
from django.utils import timezone

class Anchor(models.Model):
    name = models.TextField()
    channel_name = models.CharField(max_length=200)
    wiki = models.TextField()
    image = models.FileField()


class News_Channel(models.Model):
    name = models.TextField(blank=False)
    info = models.TextField(blank=False)
    image = models.FileField()
    website = models.TextField()
    total_star = models.PositiveIntegerField(default=0)
    total_user = models.IntegerField()


class Count(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    channelId = models.ForeignKey(News_Channel,on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)


class Review(models.Model):
    channel = models.ForeignKey(News_Channel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
