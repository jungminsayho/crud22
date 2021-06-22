from django.urls import path
from django.urls.resolvers import URLPattern

from .views import Actor3View, Movie3View

urlpatterns = [
    path('/actor', Actor3View.as_view()),
    path('/movie', Movie3View.as_view())
]