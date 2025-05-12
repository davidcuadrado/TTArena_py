from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/home.html")

def play(request):
    return render(request, "core/play.html")

def services(request):
    return render(request, "services/play.html")

def blog(request):
    return render(request, "blog/play.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")