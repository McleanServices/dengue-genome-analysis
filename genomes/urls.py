from django.urls import path
from . import views

urlpatterns = [
    path('', views.genome_list, name='genome_list'),
]
