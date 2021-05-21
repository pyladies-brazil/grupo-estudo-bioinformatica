#!/usr/bin/python3

#Complementing a Strand of DNA

seq = input("Insira a sequência nucleotídica:")

complementary = []

for i in seq:
	if i == "A":
		complementary.append("T")
	elif i == "T":
		complementary.append("A")
	elif i == "C":
		complementary.append("G")
	elif i == "G":
		complementary.append("C")
	else:
		print("O input apresenta uma letra inválida.")
		break

complementary.reverse()
complementary=''.join(complementary)

print(complementary)
 
#Computing GC Content


path = './teste.fasta'

dataset = open(path,'r')

dict={}

completeseq = ''

for line in dataset:
    line = line.strip()
    if line[0] == ">":
        if completeseq != '':
            dict[name] = completeseq
            completeseq = '' 
        name=line[1:]
        dict[name] = ''
    else:
        completeseq = completeseq + line

dict[name] = completeseq

#print(dict)

maior = 0.0

for name,seq in dict.items():
    cege = seq.count('C') + seq.count('G')
    percentage = cege * 100 /len(seq)
    if percentage > maior:
        maior = percentage
        namemax = name

print(f'{namemax}\n{maior}')
dataset.close()