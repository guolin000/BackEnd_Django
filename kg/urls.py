# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('overview/', views.overview, name='overview'),
    path('search/', views.search, name='search'),
]
