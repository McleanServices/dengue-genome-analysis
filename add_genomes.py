import os
import django
from genome_dengue import Genome_Dengue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bioinformatique2.settings')
django.setup()

from genomes.models import Genome

def add_genome(fasta_file, description=None):
    if not os.path.exists(fasta_file):
        print(f"File not found: {fasta_file}")
        return
    
    genome_dengue = Genome_Dengue(fasta_file)
    for record in genome_dengue.records:
        print(f"Processing record: {record['sequence_id']}")
        if not Genome.objects.filter(sequence_id=record['sequence_id']).exists():
            genome = Genome(
                sequence_id=record['sequence_id'],
                description=description if description else record['description'],
                a_percent=record['a_percent'],
                t_percent=record['t_percent'],
                c_percent=record['c_percent'],
                g_percent=record['g_percent'],
                gc_percent=record['gc_percent'],
                at_gc_ratio=record['at_gc_ratio']
            )
            genome.save()
            print(f"Added genome: {record['sequence_id']}")
        else:
            print(f"Duplicate sequence found: {record['sequence_id']}")

# Example usage:
# Add genome by specifying the path to your real FASTA file and the description
description = (
    "Le virus de la dengue de type 1 (DENV-1) est l’un des quatre sérotypes du virus de la dengue, "
    "appartenant à la famille des Flaviviridae et au genre Flavivirus. L'isolat New Caledonia-2017-AVS-NC-100.1 "
    "a été prélevé en 2017 en Nouvelle-Calédonie. Cet isolat est spécifique à une souche circulant dans cette région, "
    "reflétant une des nombreuses variantes génétiques du DENV-1.\n\n"
    "Le virus de la dengue est transmis principalement par les moustiques du genre Aedes (notamment Aedes aegypti et Aedes albopictus), "
    "et il provoque une infection aiguë caractérisée par de la fièvre, des douleurs musculaires, des éruptions cutanées et, dans certains cas, "
    "des formes graves comme le syndrome de choc de la dengue."
)

add_genome('C:/Users/tyrec/Downloads/bioinformatique2/DVT1_NC_17_AVS_100.1.fasta', description)
