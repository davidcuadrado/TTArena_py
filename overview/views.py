from django.shortcuts import render
from .models import Project

# Create your views here.
def overview(request):
    projects = Project.objects.all()
    return render(request, "overview/overview.html", {'projects':projects})