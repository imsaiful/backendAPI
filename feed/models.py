from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone


class Anchor(models.Model):
    name = models.TextField()
    channel_name = models.CharField(max_length=200)
    wiki = models.TextField()
    image = models.FileField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class News_Channel(models.Model):
    name = models.TextField(blank=False)
    info = models.TextField(blank=False)
    image = models.FileField()
    website = models.TextField()
    total_star = models.PositiveIntegerField(default=0)
    total_user = models.IntegerField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Count(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    channelId = models.ForeignKey(News_Channel, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.channelId.name

    class Meta:
        ordering = ["-id"]


class Review(models.Model):
    channel = models.ForeignKey(News_Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date = models.TextField(default=timezone.now)

    def __str__(self):
        return self.channel


# Create your models here.

class Republic(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Indiatv(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Ndtv(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Hindustan(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Thehindu(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Zeenews(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Indianexpress(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Oneindia(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Firstpost(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Dna(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class News18(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False, unique=True)
    date = models.TextField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class IndexTop10(models.Model):
    db_keyword = models.TextField(null=False)
    db_frequency = models.PositiveIntegerField(null=False, default=0)

    def __str__(self):
        return self.db_keyword


class CategoryRatio(models.Model):
    category = models.TextField(null=False)
    value = models.FloatField(default=0)

    def __str__(self):
        return "category ratio"
