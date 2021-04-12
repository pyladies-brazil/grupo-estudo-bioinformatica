# Complementing a Strand of DNA

from Bio.Seq import Seq
dna = Seq("AAAACCCGGT")
resultado = dna.reverse_complement()
print(resultado)
