# -*- coding: utf-8 -*-
"""Exercicio_F_Vanessa

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yq_XlFQGk3wWYuugaWysqeHPQ658mwXD

#Finding a Motif in DNA
"""

s = "GATATATGCATATACTT"
t = "ATAT"

"""Usando loop for"""

tamanho_s = len(s)
tamanho_t = len(t)

for i in range(tamanho_s - tamanho_t + 1):
  motif = s[i:i+tamanho_t]
  if motif == t:
    print(i+1, end= " ")

"""Usando indexação"""

# comprimir todos os possíveis motifs para números
valores = {"A": 1,
           "C": 2,
           "G": 3,
           "T": 4}

# vai receber todos os motifs possíveis da sequência "s"
todos_motifs_possiveis = {} 

tamanho_t = len(t)
tamanho_s = len(s)

# iterar sobre "s" para extrair todos os possíveis motifs
for i in range(tamanho_s - tamanho_t + 1):
  valor = 0
  for base in s[i:i+tamanho_t]:
    valor += valores[base] 
  todos_motifs_possiveis[i+1] = [s[i:i+tamanho_t], valor] # posicao: [motif, valor]

print(todos_motifs_possiveis)

import pandas as pd

# df apenas para visualizar a indexação
pd.DataFrame(todos_motifs_possiveis).T.rename(columns={0: "motif", 1:"valor"})

# valor do "t"
valor_t = 0
for base in t:
  valor_t += valores[base]
print(valor_t)

# fazer a filtragem pelo valor
for chave, valor in todos_motifs_possiveis.items():
  if valor[0] == t and valor[1] == valor_t:
      print(chave, end=" ")