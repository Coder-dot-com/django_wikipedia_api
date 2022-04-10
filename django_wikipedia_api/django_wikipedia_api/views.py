import json
from django.http import HttpResponse

def search(request, search_term):
    data = json.dumps("hkjh")

    return HttpResponse(data, content_type="application/json")