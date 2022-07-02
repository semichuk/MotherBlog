from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging




logger = logging.getLogger(__name__)




# Create your views here.
def home(request: Request)-> HttpResponse:
    logger.debug("hello ki!debug log ")
    print(request.META.get('REMOTE_ADDR'))
    return render(request, 'blog/homeRU.html' )