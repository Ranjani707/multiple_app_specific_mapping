from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>Ruturaj is captain of csk team</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>jadeja is vice captain of csk team</h1>')
