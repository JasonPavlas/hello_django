from django.shortcuts import render
from django.http import HTTPResponse

def index(request):
    return HttpResponse("Hello World!")
