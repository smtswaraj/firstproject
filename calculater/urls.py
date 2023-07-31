from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name='home'),
    path('add/', views.add, name='add')
]