from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the spotify-grinder's index.")
    return render (request, 'index1.html') #to render a html file
