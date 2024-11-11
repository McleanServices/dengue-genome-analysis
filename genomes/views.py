from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import GenomeForm, GenomeEditForm
from .models import Genome

def homepage(request):
    return render(request, 'genomes/homepage.html')

def genome_list_view(request):
    genomes = Genome.objects.all()
    return render(request, 'genomes/genome_list.html', {'genomes': genomes})

def add_genome_view(request):
    if request.method == 'POST':
        form = GenomeForm(request.POST)
        if form.is_valid():
            sequence_id = form.cleaned_data['sequence_id']
            sequence = form.cleaned_data['sequence']
            description = form.cleaned_data['description']
            
            # Calculate percentages and ratios
            a_percent = sequence.count('A') / len(sequence) * 100
            t_percent = sequence.count('T') / len(sequence) * 100
            c_percent = sequence.count('C') / len(sequence) * 100
            g_percent = sequence.count('G') / len(sequence) * 100
            gc_percent = (c_percent + g_percent)
            at_gc_ratio = (a_percent + t_percent) / gc_percent if gc_percent != 0 else 0

            Genome.objects.create(
                sequence_id=sequence_id,
                description=description,
                a_percent=a_percent,
                t_percent=t_percent,
                c_percent=c_percent,
                g_percent=g_percent,
                gc_percent=gc_percent,
                at_gc_ratio=at_gc_ratio
            )
            return redirect('genome_list')
    else:
        form = GenomeForm()
    return render(request, 'genomes/add_genome.html', {'form': form})

def edit_genome_view(request, pk):
    genome = get_object_or_404(Genome, pk=pk)
    if request.method == 'POST':
        form = GenomeEditForm(request.POST, instance=genome)
        if form.is_valid():
            form.save()
            return redirect('genome_list')
    else:
        form = GenomeEditForm(instance=genome)
    return render(request, 'genomes/edit_genome.html', {'form': form})

def compare_genomes(request):
    genomes = Genome.objects.all()
    return render(request, 'genomes/compare_genomes.html', {'genomes': genomes})

def genome_details(request, pk):
    genome = get_object_or_404(Genome, pk=pk)
    data = {
        'sequence_id': genome.sequence_id,
        'description': genome.description,
        'a_percent': genome.a_percent,
        't_percent': genome.t_percent,
        'c_percent': genome.c_percent,
        'g_percent': genome.g_percent,
        'gc_percent': genome.gc_percent,
        'at_gc_ratio': genome.at_gc_ratio,
    }
    return JsonResponse(data)

@require_http_methods(["DELETE"])
def delete_genome(request, pk):
    try:
        genome = Genome.objects.get(pk=pk)
        genome.delete()
        return JsonResponse({'success': True})
    except Genome.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Genome not found'}, status=404)
