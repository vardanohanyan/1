from django.shortcuts import render
from django.http import HttpResponse

def home(requests):
    return HttpResponse('<h1>Hello, Home</h1>')


def about(requests):
    return HttpResponse('<h1>About, Page</h1>')
