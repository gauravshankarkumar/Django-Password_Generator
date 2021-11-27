from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello Alien")

def gsk(request):
    return HttpResponse("<h1> Hello Gaurav </h1>")    