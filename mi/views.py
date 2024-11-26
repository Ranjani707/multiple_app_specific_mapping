from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>Rohit is captain of mi team</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>hardik pandya is vice captain of mi team</h1>')