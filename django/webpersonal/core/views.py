from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1><h2>Portada</h2>")
