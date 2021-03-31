## montando a lista com as sequencias fasta
f = open('arquivo',"r").readlines()
f.append('>FIM\n') # armengue para ler a ultima sequência

header=''
seq=''
seqs = []
        
for line in f:
    if line[0] == '>':
        if header!='':
            seqs.append(seq)
        header = line.rstrip()
        header = header[1:]
        seq =''
    else:
        seq += line.rstrip() 


## construindo o profile
A = [0]*len(seqs[0])
T = [0]*len(seqs[0])
G = [0]*len(seqs[0])
C = [0]*len(seqs[0])


for x in seqs:
  n = 0
  for nucleotideo in x:
    if nucleotideo == 'A':
      A[n]+=1
    elif nucleotideo =='T':
      T[n]+=1
    elif nucleotideo =='C':
      C[n]+=1
    elif nucleotideo =='G':  
      G[n]+=1
    n+=1

## construindo o consenso ---- essa parte está bem ineficiente, no pior dos casos, se o profile for "A =1, T=2, C=3, G=4" e o consenso for 'GGGG..G' esse código vai reescrever 4 vezes

consensus = ''
for x in range(len(A)):
  c = 'A'
  if T[x] > A[x]:
    c = 'T'
  if C[x] > T[x] and C[x] > A[x]:
    c = 'C'
  if G[x] > C[x] and G[x] > T[x] and G[x] > A[x]:
    c = 'G'
  consensus+=c

# formatar o resultado
print(consensus)
print('A:', *A, sep=" ")
print('C:', *C, sep=" ")
print('G:', *G, sep=" ")
print('T:', *T, sep=" ")

#print('T:', " ".join(["{}"]*len(T)).format(*T)) ## eu tinha formatado assim, mantendo aqui só por referencia
