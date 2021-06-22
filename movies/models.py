from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import DateField, IntegerField

## 중간테이블 사용

class Actor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'actors'


class Movie(models.Model):
    title = models.CharField(max_length=20)
    release_date = models.DateField()  # attribute
    running_time = models.IntegerField()  #attribute

    class Meta:
        db_table = 'movies'


class ActorMovie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actors_movies'


## ManyToManyField 사용

class Actor3(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'actors3'


class Movie3(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    running_time = models.IntegerField()
    actors = models.ManyToManyField(Actor3)

    class Meta:
        db_table = 'movies3'