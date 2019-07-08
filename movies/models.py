from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    """Model representing a movie."""
    title = models.CharField(max_length=50)

    year = models.IntegerField(
        verbose_name=_('Year of release'),
        help_text=_('Year of release')
    )

    released = models.DateField(
        verbose_name=_('Release date'),
        help_text=_('Release date')
    )

    runtime = models.CharField(max_length=10)

    genre = models.CharField(max_length=50)

    director = models.CharField(max_length=50)

    writer = models.CharField(max_length=50)

    actors = models.TextField()

    plot = models.TextField(max_length=1000)

    language = models.CharField(max_length=20)

    country = models.CharField(max_length=50)

    awards = models.TextField()

    poster = models.URLField()

    metascore = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name=_('Metacritic score')
    )

    imdb_rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name=_('IMDb rating')
    )

    imdb_votes = models.IntegerField(verbose_name=_('IMDb votes'))

    imdb_id = models.CharField(max_length=20)

    dvd = models.DateField(verbose_name=_('DVD release date'))

    box_office = models.CharField(max_length=20)

    production = models.CharField(max_length=50)

    website = models.URLField()


class Rating(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    source = models.CharField(
        verbose_name=_('Rating source'),
        max_length=20
    )

    value = models.CharField(
        verbose_name=_('Rating value'),
        max_length=10
    )
