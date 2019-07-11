from rest_framework.exceptions import APIException


class MissingQueryParamsException(APIException):
    """Exception raised when required query params are missing."""
    status_code = 400
    default_detail = 'Missing query parameters.'
    default_code = 'missing_query_params'


class OMDBApiException(APIException):
    """Exception raised when error occurred in OMDb API."""
    status_code = 400
    default_detail = 'Error occurred during requesting OMDb API.'
    default_code = 'omdb_error'
