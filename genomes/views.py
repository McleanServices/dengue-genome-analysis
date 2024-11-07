from django.shortcuts import render
from .models import Genome

def genome_list(request):
    genomes = Genome.objects.all()
    return render(request, 'genomes/genome_list.html', {'genomes': genomes})
