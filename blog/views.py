from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.
def home(request: Request)-> HttpResponse:
    print(request.META.get('REMOTE_ADDR'))
    return render(request, 'blog/homeRU.html' )