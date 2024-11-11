from django.urls import path
from .views import add_genome_view, genome_list_view, homepage, edit_genome_view, compare_genomes, genome_details, delete_genome

urlpatterns = [
    path('', homepage, name='homepage'),
    path('genomes/', genome_list_view, name='genome_list'),
    path('genomes/add/', add_genome_view, name='add_genome'),
    path('genomes/edit/<int:pk>/', edit_genome_view, name='edit_genome'),
    path('compare_genomes/', compare_genomes, name='compare_genomes'),
    path('genomes/<int:pk>/', genome_details, name='genome_details'),
    path('genomes/delete/<int:pk>/', delete_genome, name='delete_genome'),
]
