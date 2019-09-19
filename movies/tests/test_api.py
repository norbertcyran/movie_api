from datetime import datetime
from unittest import mock

from django.urls import reverse
from rest_framework.test import APITestCase

from .fixtures import PREPROCESSED_RESPONSE
from ..exceptions import OMDBApiException
from ..models import Comment


class MoviesAPITestCase(APITestCase):
    """Movies API endpoints tests."""
    fixtures = ['test_movies']

    def test_top_no_params(self):
        """Top movies endpoint raises exception when no params are provided."""
        url = reverse('top-movies')
        response = self.client.get(url, format='json')

        self.assertContains(response, 'Missing query params', status_code=400)

    def test_top_ok(self):
        """Top endpoint returns movies sorted and ranked by comment count."""
        self.maxDiff = None
        self._create_comments()
        query_string = '?from=2019-07-01&to=2019-07-05'
        url = reverse('top-movies')
        response = self.client.get(url + query_string, format='json')

        expected = [
            {'movie': 1, 'total_comments': 2, 'rank': 1},
            {'movie': 2, 'total_comments': 2, 'rank': 1},
            {'movie': 3, 'total_comments': 0, 'rank': 2},
            {'movie': 4, 'total_comments': 0, 'rank': 2}
        ]

        self.assertListEqual(expected, response.data)

    @mock.patch('movies.serializers.fetch_movie_data')
    def test_create_movie(self, fetch_mock):
        """Movie is fetched from OMDb and inserted into app db."""
        fetch_mock.return_value = PREPROCESSED_RESPONSE

        path = reverse('movie-list')
        response = self.client.post(path, data={'title': 'Clockwork orange'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'A Clockwork Orange')

    @mock.patch('movies.serializers.fetch_movie_data')
    def test_create_movie__api_exception(self, fetch_mock):
        """Response with 400 status code and error message is returned."""
        fetch_mock.side_effect = OMDBApiException('Movie not found.')

        path = reverse('movie-list')
        response = self.client.post(path, data={'title': 'Non existent'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Movie not found.')

    @staticmethod
    def _create_comment(movie_id, created):
        comment = Comment.objects.create(movie_id=movie_id, body='test')
        comment.created = created
        comment.save()
        return comment

    def _create_comments(self):
        self._create_comment(movie_id=1, created=datetime(2019, 7, 1, 12, 0, 0))
        self._create_comment(movie_id=1, created=datetime(2019, 7, 2, 12, 0, 0))
        self._create_comment(movie_id=2, created=datetime(2019, 7, 3, 12, 0, 0))
        self._create_comment(movie_id=2, created=datetime(2019, 7, 4, 12, 0, 0))
        self._create_comment(movie_id=3, created=datetime(2019, 7, 5, 12, 0, 0))
