from Bio import SeqIO
from Bio.SeqUtils import GC

print(max(((r.id, GC(r.seq)) for r in SeqIO.parse("dna","fasta")),key=lambda x : x[1]))