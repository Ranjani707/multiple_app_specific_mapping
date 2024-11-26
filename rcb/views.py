from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>Virat Kholi is captain of rcb team</h1>')

def vicecaptain(request):
    return HttpResponse('<h1> K.L.Rahul is vice captain of rcb team</h1>')
