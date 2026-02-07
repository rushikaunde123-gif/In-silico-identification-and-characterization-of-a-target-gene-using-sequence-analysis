from Bio import SeqIO

record = SeqIO. read("sequence.fasta", "fasta")

print("Sequence ID:", record.id)
print("sequence")
print(record.seq)
print("Sequence Length:", len(record.seq))