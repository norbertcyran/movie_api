from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from movies.exceptions import MissingQueryParamsException
from .models import Movie, Comment
from .serializers import CreateMovieSerializer, MovieSerializer, CommentSerializer


class MovieListView(ListCreateAPIView):
    """API view for listing and creating movies."""
    queryset = Movie.objects.all()
    filterset_fields = ('title', )
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('title', 'imdb_votes', 'year', 'imdb_rating', 'metascore')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateMovieSerializer
        return MovieSerializer

    def create(self, request, *args, **kwargs):
        """Fetch movie from OMDb and add it to application's DB."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        instance = serializer.instance
        serializer = MovieSerializer(instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filterset_fields = ('movie', )


class TopMoviesView(APIView):
    """
    API View for displaying top movies.

    Top movies ranked by total comments count in specified date range.
    """
    def get(self, request, *args, **kwargs):
        """
        Get top movies.

        Query params (required):
            from, to - date range of comments being ranked.
        """
        try:
            from_date = self.request.query_params['from']
            to_date = self.request.query_params['to']
        except KeyError:
            raise MissingQueryParamsException("Missing query params 'from' and 'to")
        comment_filter = Q(comments__created__gte=from_date, comments__created__lte=to_date)
        movies = Movie.objects.annotate(
            total_comments=Count('comments', filter=comment_filter)
        ).order_by('-total_comments')
        data = []
        rank = 0
        prev_total = None
        for movie in movies:
            if movie.total_comments != prev_total or prev_total is None:
                rank += 1
            data.append({
                'movie': movie.id,
                'total_comments': movie.total_comments,
                'rank': rank
            })
            prev_total = movie.total_comments
        return Response(data)
