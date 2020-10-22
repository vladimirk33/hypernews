from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.


def index_view(request):
    return HttpResponse("Coming soon")


def show_news(request):
    with open(settings.NEWS_JSON_PATH, 'r') as file:
        pass