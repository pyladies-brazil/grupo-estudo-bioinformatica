import math

k = int(input("Type the number of homozygous dominant: "))
m = int(input("Type the number of heterozygous: "))
n = int(input("Type the number of homozygous recessive: "))

population = k + m + n

#combination formula
total_combination = factorial(population)/(factorial(2)*factorial((population-2)))

if k>=2:
  AA_combinations =  factorial(k)/(factorial(2)*factorial((k-2))) + (k * m) + (k * n)
  AaAa_combinations = factorial(m)/(factorial(2)*factorial((m-2)))
  Aaaa_combinations = (m * n)
elif k==1:
  AA_combinations = (k * m) + (k * n)

prob_AA_combinations_dominant = AA_combinations / total_combination
prob_AaAa_combinations_dominant = (AaAa_combinations / total_combination) * (3/4)
prob_Aaaa_combinations_dominant = (Aaaa_combinations / total_combination) * (2/4)

total_combinations_dominant = prob_AA_combinations_dominant + prob_AaAa_combinations_dominant + prob_Aaaa_combinations_dominant
print("{0:.5f}".format(total_combinations_dominant))


