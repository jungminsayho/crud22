from django.urls import path, include
from django.urls.resolvers import URLPattern

from .views import OwnersView, DogsView

urlpatterns = [
    path('', OwnersView.as_view()),
    path('/dogs', DogsView.as_view())
]