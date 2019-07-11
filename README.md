## MovieDB API

Django application fetching movie data from [Open Movie DB](http://omdbapi.com). 
Application stores fetched movies in its own database. User can add comments to the
movie and retrieve a list of top movies sorted by comments count.


### Build
1. Create .env file with `SECRET_KEY<key>` and `OMDB_API_KEY=<key>`
and `DEBUG=True`
#### With Docker
1. `docker build -t movie_api .`
2. `docker-compose run --rm web python /app/manage.py migrate`
3. `docker-compose up -d`
#### Locally
1. `pipenv install`
2. `python manage.py migrate`
3. `python manage.py runserver`

#### Production
Steps like above, but don't include `DEBUG=True` in .env and run 
`python manage.py collectstatic`
