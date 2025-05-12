from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/home.html")

def play(request):
    return render(request, "core/play.html")

def services(request):
    return render(request, "core/services.html")

def blog(request):
    return render(request, "core/blog.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")