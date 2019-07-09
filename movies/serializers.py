from rest_framework import serializers

from .utils import fetch_movie_data
from .models import Rating, Movie


class RatingSerializer(serializers.ModelSerializer):
    """Serializer for Rating model."""
    class Meta:
        model = Rating
        fields = ('source', 'value')


class MovieSerializer(serializers.ModelSerializer):
    """Serializer for Movie model."""
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'rated', 'year', 'released', 'runtime', 'genre', 'director',
                  'writer', 'actors', 'plot', 'language', 'country', 'awards',
                  'poster', 'ratings', 'metascore', 'imdb_rating', 'imdb_votes',
                  'imdb_id', 'dvd', 'box_office', 'production', 'website')

    def create(self, validated_data):
        ratings = validated_data.pop('ratings')

        movie = Movie.objects.create(**validated_data)

        for rating in ratings:
            Rating.objects.create(movie=movie, **rating)

        return movie


class CreateMovieSerializer(serializers.ModelSerializer):
    """Serializer saving movies fetched from OMDb to database."""
    class Meta:
        model = Movie
        fields = ('title', )

    def create(self, validated_data):
        movie_data = fetch_movie_data(validated_data['title'])
        movie_serializer = MovieSerializer(data=movie_data)
        movie_serializer.is_valid(raise_exception=True)
        movie = movie_serializer.save()
        return movie
