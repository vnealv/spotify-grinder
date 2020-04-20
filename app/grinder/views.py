from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .api_wrapper import get_track_list

def index(request):
    #return HttpResponse("Hello, world. You're at the spotify-grinder's index.")
    '''
    if no query_filter is provided in the request we query with the default track filter
    validations of the query are handled by the api_wrapper instead of the view.
    '''
    search_query = request.GET.get('q')
    query_filter = request.GET.get('filter')
    if not query_filter:
        query_filter = 'track'

    count, items = get_track_list(search_query, query_filter)
    context = {
        'count' : count,
        'items': items,
        'q': search_query,
        'filter' : query_filter
    }
    return render(request, 'index2.html', context)
