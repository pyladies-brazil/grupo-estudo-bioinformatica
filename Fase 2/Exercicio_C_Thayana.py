from Bio import SeqIO
import numpy as np 
import pandas as pd
import os

path = os.path.dirname(__file__)
matrix = np.zeros(shape=(4,len(next(SeqIO.parse(f"{path}/rosalind_test.txt", "fasta")).seq)), dtype=int)
df_matrix = pd.DataFrame(matrix, index=['A', 'C', 'G', 'T'])
print(df_matrix)

'''for record in SeqIO.parse(f"{path}/rosalind_test.txt", "fasta"):
    for count, nucleotide in enumerate(record.seq):
        df_matrix[count][nucleotide] += 1 

seq_consensus = ''.join(i for i in list(df_matrix.idxmax(axis=0)))
df_matrix.insert(0,'',['A:', 'C:', 'G:', 'T:'])

with open(f"{path}/output.csv", "w") as file_final:
    file_final.write(f'{seq_consensus}\n')
    df_matrix.to_csv(file_final, sep = ' ', index=False, header=False)'''
      
