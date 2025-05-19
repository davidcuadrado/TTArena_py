from django.urls import path
from . import views
from core import views as core_views
from overview import views as overview_views
from services import views as services_views

urlpatterns = [
    path('', core_views.home, name="home"),
    path('play/', core_views.play, name="play"),
    path('about/', core_views.about, name="about"),
    path('contact/', core_views.contact, name="contact"),
]
