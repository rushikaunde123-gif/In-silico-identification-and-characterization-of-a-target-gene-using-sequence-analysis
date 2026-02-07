from Bio import SeqIO, Entrez
from Bio.Blast import NCBIXML

Entrez.email = "your_email@gmail.com"

with open("blast_output.xml") as result_handle:
    blast_record = NCBIXML.read(result_handle)

top_alignment = blast_record.alignments[0]
top_hsp = top_alignment.hsps[0]

accession = top_alignment.accession

print("Top BLAST Hit Accession:", accession)
print("E-value:", top_hsp.expect)
print("Identity:", top_hsp.identities)

print("\nFetching functional annotation from NCBI...\n")

handle = Entrez.efetch(
    db="nucleotide", 
    id=accession, 
    rettype="gb", 
    retmode="text"
)

record = SeqIO.read(handle, "genbank")
handle.close()

for feature in record.features:
    if feature.type =="gene":
        gene_name = feature.qualifiers.get("gene", ["N/A"])[0]
        print("Gene Name:", gene_name)

        if feature.type =="CDS":
            product = feature.qualifiers.get("product", ["N/A"])[0]
            protein_id = feature.qualifiers.get("protein-id", ["N/A"])[0]
            print("Protein_ID:", protein_id)
            print("Function / Product:", product)
