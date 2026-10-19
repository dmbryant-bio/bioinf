k=int(input('Enter the number of homozygous dominant individuals (k): '))
m=int(input('Enter the number of heterozygous individuals (m): '))
n=int(input('Enter the number of homozygous recessive individuals (n): '))
population_size=k+m+n
#probability=(k/population_size)*((k-1)/(population_size-1))+((k/population_size)*(m/(population_size-1)))+((m/population_size)*(k/(population_size-1)))+((m/population_size)*((m-1)/(population_size-1))*0.75)
recessive = (
    (m / population_size) * ((m - 1) / (population_size - 1)) * 0.25
    + 2 * (m / population_size) * (n / (population_size - 1)) * 0.5
    + (n / population_size) * ((n - 1) / (population_size - 1))
)
probability = 1 - recessive
print(probability)