#!/usr/bin/python3

#E - Mendel's First Law

# k  individuals are homozygous dominant, m are heterozygous, and n are homozygous recessive

k = float(input("Entre k:"))
m = float(input("Entre m:"))
n = float(input("Entre n:"))

total = k + m + n

#Evento X - Probabilidade do primeiro organismo de ser dominante, heterozigotico ou recessivo
dominant = k/total
hetero = m/total
recessive = n/total

#Evento Y - Probabilidade do segundo organismo
total2 = total - 1 #tiro 1 do total já que o primeiro já foi sorteado

dominant2 = dominant*((k-1)/total2) + dominant*(m/total2) + dominant*(n/total2) # AAxAA / AAxAa / AAxaa

hetero2 = hetero*(k/total2) + 0.75*(hetero*((m-1)/total2)) + 0.5*(hetero*(n/total2)) #AaxAA / AaxAa produz 75% dominante / Aaxaa produz 50% dominante

recessive2 = recessive*(k/total2) + 0.5*(recessive*(m/total2)) # aaxAA / aaxAa 50% dominante 

probabilidade = round(dominant2 + hetero2 + recessive2 , 5)

#The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
print (f'{probabilidade}')