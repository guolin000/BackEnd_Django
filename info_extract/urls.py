# book/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('predict', views.predict, name='predict'),
    path('save', views.save, name='save'),
]
