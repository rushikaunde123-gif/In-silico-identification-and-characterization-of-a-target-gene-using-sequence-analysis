from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

record = SeqIO.read("sequence.fasta","fasta")

print("sequence ID:", record.id)
print("Description:", record.description)
print("sequence:", record.seq)

print("sequence Length:",len(record.seq))
gc =gc_fraction(record.seq)*100
print("GC Content:{:.2f}%".format(gc))

print("complement:", record.seq.complement())
print("Reverse Complement:", record.seq.reverse_complement())

print("RNA Sequence:", record.seq.transcribe())
print("Protein Sequence:", record.seq.translate(to_stop=True))

print("A:", record.seq.count("A"))
print("T:", record.seq.count("T"))
print("G:", record.seq.count("G"))
print("C:", record.seq.count("C"))


