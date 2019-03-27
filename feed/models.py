from django.db import models


# Create your models here.

class Anchor(models.Model):
    name = models.TextField()
    channel_name = models.CharField(max_length=200)
    wiki = models.TextField()
    image = models.FileField()

