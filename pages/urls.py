from django.urls import path
from . import views

urlpatterns = [
    path('', views.page, name='pages'),
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
]