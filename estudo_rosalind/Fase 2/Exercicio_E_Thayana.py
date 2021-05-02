
from Bio import SeqIO, ExPASy
import os
import time

path = os.path.dirname(__file__)
ids_file = open(rf'{path}\Rosalind.txt', 'r')
ids_list = [line.strip() for line in ids_file]

def extract_sequence_biopython(id):
    with ExPASy.get_sprot_raw(id) as handle:
        seq_record = SeqIO.read(handle, "swiss")
    return seq_record.seq

def find_Motif(seq_id, seq):
    indexMotif_string = ""
    for i in range(len(seq)):
        if (seq[i] == 'N') and (seq[i+2] == 'S' or seq[i+2] == 'T'):
            if seq[i+1] != 'P' and seq[i+3] != 'P':
                indexMotif_string += f"{i+1} "
    if len(indexMotif_string) != 0:
        print(f"{id}\n{indexMotif_string}")
        
for id in ids_list:
    seq = extract_sequence_biopython(id)
    find_Motif(id, seq)
