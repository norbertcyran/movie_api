from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    """Model representing a movie."""
    title = models.CharField(max_length=50)

    rated = models.CharField(max_length=2, null=True, blank=True)

    year = models.IntegerField(
        verbose_name=_('Year of release'),
        help_text=_('Year of release')
    )

    released = models.DateField(
        verbose_name=_('Release date'),
        help_text=_('Release date')
    )

    runtime = models.CharField(max_length=10)

    genre = models.CharField(max_length=200)

    director = models.CharField(max_length=200)

    writer = models.CharField(max_length=200)

    actors = models.TextField()

    plot = models.TextField(max_length=1000)

    language = models.CharField(max_length=200)

    country = models.CharField(max_length=200)

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

    production = models.CharField(max_length=200)

    website = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Rating(models.Model):
    """Model representing movie rating."""
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    source = models.CharField(
        verbose_name=_('Rating source'),
        max_length=100
    )

    value = models.CharField(
        verbose_name=_('Rating value'),
        max_length=10
    )


class Comment(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
