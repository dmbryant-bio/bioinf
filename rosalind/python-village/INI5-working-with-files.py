with open('C:\\Users\\spark\\Git Bioinformatics\\bioinf\\rosalind\\python-village\\rosalind_ini5.txt', 'r') as f:
    for i, line in enumerate(f):
        if i % 2 != 0:
            print(line.strip())
