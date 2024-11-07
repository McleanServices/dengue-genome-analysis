import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bioinformatique2.settings')
django.setup()

from genomes.models import Genome

def remove_duplicates():
    seen = set()
    duplicates = []
    for genome in Genome.objects.all():
        if genome.sequence_id in seen:
            duplicates.append(genome.id)
        else:
            seen.add(genome.sequence_id)
    
    Genome.objects.filter(id__in=duplicates).delete()
    print(f"Removed {len(duplicates)} duplicate entries.")

# Run the script to remove duplicates
remove_duplicates()
