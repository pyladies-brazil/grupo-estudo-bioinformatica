from Bio import SeqIO
from Bio.Seq import Seq
import os

path_file = os.path.dirname(__file__)

handle = (SeqIO.parse(f"{path_file}/rosalind_splc.txt", "fasta"))

for count, seq_record in enumerate(handle):
    if count == 0:
        general_seq = str(seq_record.seq)
    else:
        general_seq = general_seq.replace(str(seq_record.seq), '')

general_seq = Seq(general_seq)
print(general_seq.translate(to_stop=True))

        

 
    
