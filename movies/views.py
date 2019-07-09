from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Movie
from .serializers import CreateMovieSerializer, MovieSerializer


class MovieListView(ListCreateAPIView):
    """API view for listing and creating movies."""
    queryset = Movie.objects.all()

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


