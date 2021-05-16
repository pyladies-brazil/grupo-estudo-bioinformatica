#!/usr/bin/python3

#D - Rabbits and Recurrence Relations

meses = int(input("Entre n≤40:"))
pares_ninhada = int(input("Entre k≤5:"))

pares_filhotes = 1
pares_adultos = 0
total_pares = 1

for i in range(1,meses):
    ninhada = pares_adultos*pares_ninhada
    pares_adultos = pares_adultos + pares_filhotes
    pares_filhotes = ninhada
    total_pares = pares_adultos + pares_filhotes
    
print(total_pares)