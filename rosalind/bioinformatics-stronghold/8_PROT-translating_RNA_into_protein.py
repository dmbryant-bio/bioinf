from pathlib import Path

file_path = Path(__file__).parent / "rna_codon_table.txt"

codon_dict = {}

with open(file_path) as f:
    for line in f:
        data = line.split()

        for i in range(0, len(data), 2):
            codon_dict[data[i]] = data[i + 1]

rna_str = input('Enter an RNA string: ')
protein_str = ""

for i in range(0, len(rna_str), 3):
    codon = rna_str[i:i+3]
    if codon in codon_dict:
        amino_acid = codon_dict[codon]
        if amino_acid == 'Stop':
            break
        protein_str += amino_acid

print(protein_str)