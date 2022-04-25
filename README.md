# django_wikipedia_api

To deploy locally simply use python manage.py runserver.

The API only has one route /{search_term} and uses bs4 to return the first page of wikipedia search results as a json.
{search_term} must not contain '/'.
