from django.shortcuts import render
from django.http import JsonResponse
import requests

def test(request):
        key="4589d737"
        url= f"http://www.omdbapi.com/?apikey={key}&s=harry potter"
        response= requests.get(url).json()
        context = {
                'movies': response,
        }
        return render(request, "list.html", context)
