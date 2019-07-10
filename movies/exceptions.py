from rest_framework.exceptions import APIException


class MissingQueryParamsException(APIException):
    """Exception raised when required query params are missing."""
    status_code = 400
    default_detail = 'Missing query parameters.'
    default_code = 'missing_query_params'


class MovieNotFoundException(APIException):
    """Exception raised when movie was not found in OMDb."""
    status_code = 404
    default_detail = 'Movie with such title was not found in OMDb.'
    default_code = 'movie_not_found'
