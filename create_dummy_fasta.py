import os

dummy_fasta_content1 = """>sequence_1
ATCGATCGATCG
>sequence_2
GCTAGCTAGCTA
"""

dummy_fasta_content2 = """>sequence_3
TTGGAATTCCGG
>sequence_4
CCGGAATTGGCC
"""

fasta_file1_path = 'C:/Users/tyrec/Downloads/bioinformatique2/fasta_file1.fasta'
fasta_file2_path = 'C:/Users/tyrec/Downloads/bioinformatique2/fasta_file2.fasta'

with open(fasta_file1_path, 'w') as f:
    f.write(dummy_fasta_content1)
    print(f"Created {fasta_file1_path}")

with open(fasta_file2_path, 'w') as f:
    f.write(dummy_fasta_content2)
    print(f"Created {fasta_file2_path}")

# Verify that the files were created
if os.path.exists(fasta_file1_path):
    print(f"Verified: {fasta_file1_path} exists")
else:
    print(f"Error: {fasta_file1_path} does not exist")

if os.path.exists(fasta_file2_path):
    print(f"Verified: {fasta_file2_path} exists")
else:
    print(f"Error: {fasta_file2_path} does not exist")
