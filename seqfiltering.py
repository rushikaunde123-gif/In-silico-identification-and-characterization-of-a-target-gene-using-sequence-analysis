from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

MIN_LENGTH = 300

record = SeqIO.read("sequence.fasta", "fasta")
seq = record.seq

print("sequence ID:", record.id)
print("sequence length:", len(seq))

gc = gc_fraction(seq) *100
print("GC content:", round(gc, 2), "%")

if len(seq)< MIN_LENGTH:
    print("sequence is too short for downstream nalysis")
else:
    print("sequence is suitable for further analysis")