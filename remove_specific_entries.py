import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bioinformatique2.settings')
django.setup()

from genomes.models import Genome

def remove_specific_entries():
    sequence_ids_to_remove = [
        'sequence_1',
        'sequence_2',
        'sequence_3',
        'sequence_4',
        'sequence_DVT1-NC-17-AVS-100.1'
    ]
    
    deleted_count, _ = Genome.objects.filter(sequence_id__in=sequence_ids_to_remove).delete()
    print(f"Removed {deleted_count} entries.")

# Run the script to remove specific entries
remove_specific_entries()
