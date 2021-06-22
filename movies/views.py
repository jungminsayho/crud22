import json
from django.db.models.fields import DateField

from django.http import JsonResponse
from django.views import View
from movies.models import Actor, Movie, ActorMovie
from movies.models import Actor3, Movie3


## 중간테이블 사용

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            movies = actor.actormovie_set.all()
            results.append(
                {
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "movies": [movie.movie.title for movie in movies]
                }
            )
        return JsonResponse({'results': results}, status=200)



class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actors = movie.actormovie_set.all()
            results.append(
                {
                    "title": movie.title,
                    "running_time": movie.running_time,
                    "actors": [actor.actor.first_name + ' ' + actor.actor.last_name for actor in actors]
                }
            )
        return JsonResponse({'results': results}, status=200)
    


# ManyToManyField 사용

class Actor3View(View):
    def get(self, request):
        actors = Actor3.objects.all()
        results = []
        for actor in actors:
            movies = actor.movie3_set.all()
            movie_list = []
            for movie in movies:
                movie_list.append(movie.title)

            results.append(
                {
                    'first_name': actor.first_name,
                    'last_name': actor.last_name,
                    'date_of_birth': actor.date_of_birth,
                    'movies': movie_list                }
            )
        return JsonResponse({'results': results}, status=200)


class Movie3View(View):
    def get(self, request):
        movies = Movie3.objects.all()
        results = []
        for movie in movies:
            actors = movie.actors.all()
            actor_list = []
            for actor in actors:
                actor_list.append(actor.first_name + ' ' + actor.last_name)

            results.append(
                {
                    'title': movie.title,
                    'release_date': movie.release_date,
                    'running_time': movie.running_time,
                    'actors': actor_list
                }
            )
        return JsonResponse({'results': results}, status=200)