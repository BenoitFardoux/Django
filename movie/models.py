from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre)

