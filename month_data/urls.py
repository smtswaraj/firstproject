from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('/january', views.january, name='display'),
    # path('/february', views.february, name='display'),
    # path('/march', views.march, name='display'),
    path('', views.index, name = 'index'),
    path('/<int:month>', views.month_with_num),
    path('/<str:month>', views.monthes, name='dis'),
]