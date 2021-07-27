from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nearest(request):
    return HttpResponse("The nearest distance between two points is zero.")
