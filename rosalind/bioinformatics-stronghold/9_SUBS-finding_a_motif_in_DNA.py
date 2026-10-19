dnaseq = input('Enter a DNA string: ')
dnamotif = input('Enter a DNA motif: ')

positions = []
for i in range(len(dnaseq) - len(dnamotif) + 1):
    if dnaseq[i:i + len(dnamotif)] == dnamotif:
        positions.append(i + 1)

print(*positions)