from unittest import mock

from django.test import TestCase

from .fixtures import OMDB_RESPONSE_MOCK, PREPROCESSED_RESPONSE
from .. import utils


class UtilsTestCase(TestCase):
    """Test case for utils module."""
    def test_convert_to_snake_case(self):
        """Camel case strings are converted to snake case."""
        camel_case_input = ['CamelCase', 'camelCaseCase', 'CamelCASE']
        expected = ['camel_case', 'camel_case_case', 'camel_case']
        actual = [utils.convert_to_snake_case(el) for el in camel_case_input]
        self.assertListEqual(actual, expected)

    @mock.patch('requests.get')
    def test_fetch_movie_data(self, get_mock):
        """Preprocessed movie data dict is returned."""
        get_mock.return_value = mock.Mock(
            json=mock.Mock(return_value=OMDB_RESPONSE_MOCK)
        )
        data = utils.fetch_movie_data('Clockwork orange')
        self.assertDictEqual(data, PREPROCESSED_RESPONSE)
