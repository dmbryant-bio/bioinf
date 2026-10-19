dna_str = input('Enter a DNA string: ')
rev_comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
rev_comp_str = dna_str.translate(str.maketrans(rev_comp_dict))[::-1]
print(rev_comp_str)
