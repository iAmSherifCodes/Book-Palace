from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, 'hello.html')


def hello(request):
    return HttpResponse("Welcome to our playground")
