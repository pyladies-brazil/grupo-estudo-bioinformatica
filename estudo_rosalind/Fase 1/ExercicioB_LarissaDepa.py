# Complementing a Strand of DNA

from Bio.Seq import Seq
dna = Seq("AAAACCCGGT")
print(dna.reverse_complement())
