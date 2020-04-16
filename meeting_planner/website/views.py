from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})
#    return HttpResponse("Hola como estan, ustedes son pareja")


def date(request):
    return HttpResponse("This page was served at" + str(datetime.now()))


# Por favor aniade: Alguna agina que mostrara algun texto acerca de ti
def self(resquest):
    return HttpResponse("La suma de dos numeros es.... ")