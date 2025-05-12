from django.urls import path
from . import views
from core import views as core_views
from overview import views as overview_views

urlpatterns = [
path('', core_views.home, name="home"),
    path('play/', core_views.play, name="play"),
    path('services/', core_views.services, name="services"),
    path('blog/', core_views.blog, name='blog'),
    path('about/', core_views.about, name="about"),
    path('overview/', overview_views.overview, name="overview"),
    path('contact/', core_views.contact, name="contact"),
]