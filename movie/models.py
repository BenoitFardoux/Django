from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    poster = models.ImageField()
    genre = models.CharField(max_length=500)
