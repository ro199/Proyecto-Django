from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def welcome(request):
    return HttpResponse("Hola como estan, ustedes son pareja")

def date(request):
    return HttpResponse("This page was served at" + str(datetime.now()))


# Por favor aniade: Alguna agina que mostrara algun texto acerca de ti
def self(resquest):
    return HttpResponse("La suma de dos numeros es.... ")