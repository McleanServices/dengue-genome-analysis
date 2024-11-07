from Bio import SeqIO

class Genome_Dengue:
    def __init__(self, fasta_file):
        self.fasta_file = fasta_file
        self.records = []
        self._parse_fasta()

    def _parse_fasta(self):
        for record in SeqIO.parse(self.fasta_file, "fasta"):
            sequence = str(record.seq)
            a_percent = (sequence.count('A') / len(sequence)) * 100
            t_percent = (sequence.count('T') / len(sequence)) * 100
            c_percent = (sequence.count('C') / len(sequence)) * 100
            g_percent = (sequence.count('G') / len(sequence)) * 100
            gc_percent = ((sequence.count('G') + sequence.count('C')) / len(sequence)) * 100
            at_gc_ratio = (sequence.count('A') + sequence.count('T')) / (sequence.count('G') + sequence.count('C'))
            self.records.append({
                'sequence_id': record.id,
                'description': record.description,
                'a_percent': a_percent,
                't_percent': t_percent,
                'c_percent': c_percent,
                'g_percent': g_percent,
                'gc_percent': gc_percent,
                'at_gc_ratio': at_gc_ratio
            })

    def __str__(self):
        return '\n'.join([f"ID: {record['sequence_id']}\n"
                          f"Description: {record['description']}\n"
                          f"A%: {record['a_percent']:.2f}\n"
                          f"T%: {record['t_percent']:.2f}\n"
                          f"C%: {record['c_percent']:.2f}\n"
                          f"G%: {record['g_percent']:.2f}\n"
                          f"GC%: {record['gc_percent']:.2f}\n"
                          f"AT/GC Ratio: {record['at_gc_ratio']:.2f}\n"
                          for record in self.records])

# Example usage:
# genome = Genome_Dengue("path_to_fasta_file.fasta")
# print(genome)
