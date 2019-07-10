from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('comments', views.CommentViewSet)

urlpatterns = [
    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('top/', views.TopMoviesView.as_view(), name='top-movies')
] + router.urls
