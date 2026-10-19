nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
dna_str = input('Enter a DNA string: ')
for nucleotide in dna_str:
    nucleotides[nucleotide] += 1
print(nucleotides['A'],nucleotides['C'],nucleotides['G'],nucleotides['T'])
