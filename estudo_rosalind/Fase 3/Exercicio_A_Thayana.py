from Bio import SeqIO
from Bio.Seq import Seq
import os 
path = os.path.dirname(__file__)

with open(f'{path}/rosalind.txt', 'r') as rosalind_file:
    sequence_foward = SeqIO.read(rosalind_file, "fasta").seq
    sequence_reverse = sequence_foward.reverse_complement()

def find_start_stop_codons(sequence):
    atg_index = []
    stop_index = [] 
    for i in range(len(sequence)):
        if sequence[i:i+3] == "ATG":
            atg_index.append(i)      
        elif sequence[i:i+3] == "TAA":
            stop_index.append(i)
        elif sequence[i:i+3] == "TAG":
            stop_index.append(i)
        elif sequence[i:i+3] == "TGA":
            stop_index.append(i)
    return atg_index, stop_index

def translate_orfs(sequence, atg_index, stop_index, output):
    for start in atg_index:
        for stop in stop_index:
            if stop > start+2:
                if len(sequence[start:stop+3]) % 3 == 0:
                    seq_translate = sequence[start:stop+3]
                    output.add(str(seq_translate.translate(to_stop=True)))
                    break 
    return output

atg_index, stop_index = find_start_stop_codons(sequence_foward)              
output_foward = translate_orfs(sequence_foward, atg_index, stop_index, output= set())

atg_index, stop_index = find_start_stop_codons(sequence_reverse)              
output_total = translate_orfs(sequence_reverse, atg_index, stop_index, output_foward)

for orf in output_total:
    print(orf)

