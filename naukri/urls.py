from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name = "test"),
    path('/job', views.job_desc, name = "test"),
]