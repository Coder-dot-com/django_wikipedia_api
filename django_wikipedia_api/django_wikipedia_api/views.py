from datetime import date
import json
from django.http import HttpResponse

from .utils import search_wikipedia

def search(request, search_term):

    results = {
        "Results": search_wikipedia(search_term=search_term),
        "Date Retrieved": str(date.today()),

    }
    data = json.dumps(results)

    return HttpResponse(data, content_type="application/json")