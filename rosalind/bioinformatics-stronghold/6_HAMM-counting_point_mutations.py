dnaseq1=input('Enter the first DNA string: ')
dnaseq2=input('Enter the second DNA string: ')
hamming_distance=0

for i in range(len(dnaseq1)):
    if dnaseq1[i]!=dnaseq2[i]:
        hamming_distance+=1

print(hamming_distance)