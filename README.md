## MovieDB API

Django application fetching movie data from [Open Movie DB](http://omdbapi.com). 
Application stores fetched movies in its own database. User can add comments to the
movie and retrieve a list of top movies sorted by comments count.


### Build
1. Install pipenv if not installed
2. `pipenv sync`
3. `python manage.py runserver`