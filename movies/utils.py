import re

import requests
from django.conf import settings

OMDB_URL = 'http://omdbapi.com'

FIRST_CAP_RE = re.compile(r'(.)([A-Z][a-z]+)')
ALL_CAP_RE = re.compile(r'([a-z0-9])([A-Z])')


def fetch_movie_data(title):
    """Fetch movie data from OMDb API."""
    api_key = settings.OMDB_API_KEY
    rsp = requests.get(OMDB_URL, params={'t': title, 'apikey': api_key})
    data = preprocess_movie_data(rsp.json())
    return data


def preprocess_movie_data(data):
    """Preprocess movie data from OMDb API to be readable by MovieSerializer."""
    data = {convert_to_snake_case(key): value for key, value in data.items()
            if key not in ['Response', 'Type']}

    data['imdb_votes'] = data['imdb_votes'].replace(',', '')

    ratings = data['ratings']

    data['ratings'] = [
        {convert_to_snake_case(key): value for key, value in rating.items()}
        for rating in ratings
    ]

    return data


def convert_to_snake_case(string):
    """Convert camel case string to snake case."""
    intermediate = FIRST_CAP_RE.sub(r'\1_\2', string)
    return ALL_CAP_RE.sub(r'\1_\2', intermediate).lower()


