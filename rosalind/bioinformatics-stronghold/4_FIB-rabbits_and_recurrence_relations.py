#given positive integers n <=40 and k <=5
#Return: The total number of rabbit pairs that will be present after n
# months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
# rabbit pairs (instead of only 1 pair).
#https://rosalind.info/problems/fib/
n = int(input('Enter the number of months (n): '))
k = int(input('Enter the number of rabbit pairs produced by each pair (k): '))
f1 = 1
f2 = 1
for i in range(2,n):
    fn = f2 + k*f1
    f1 = f2
    f2 = fn
print(f2)