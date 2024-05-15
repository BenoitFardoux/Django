from django.contrib import admin
from django.urls import path

from movie import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("movies/<string:title>", views.search_movie, name='search_movie')
]