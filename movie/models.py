from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)

    @property
    def get_all_movies(self):
        return self.movie_set.all().values_list()


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre)
