from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>TTArena Home</h1><h2>Landing page<h2>")

