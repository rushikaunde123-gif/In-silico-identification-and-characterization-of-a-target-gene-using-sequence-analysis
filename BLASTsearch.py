from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

record = SeqIO.read("sequence.fasta", "fasta")

print("Running BLAST homology search...")
print("print wait, this may take a few minutes")

result_handle = NCBIWWW.qblast(
    program="blastn",
    database="nt",
    sequence=record.seq 
)

with open("blast_output.xml", "w")as out_file:
    out_file.write(result_handle.read())

result_handle.close()

print("BLAST search completed")
print("result saved in blast_output.xml")

with open("blast_output.xml") as result_handle:
    blast_record = NCBIXML.read(result_handle)

print("\n Top Homology Hits:\n")

for alignment in blast_record.alignments[:5]:
    for hsp in alignment.hsps:
        print("Title:", alignment.title)
        print("Length:", alignment.length)
        print("Score:", hsp.score)
        print("E-value:", hsp.expect)
        print("Identities:", hsp.identities)
        print("-" * 50)
