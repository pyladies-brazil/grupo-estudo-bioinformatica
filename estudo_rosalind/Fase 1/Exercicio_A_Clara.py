
# Counting DNA Nucleotides - http://rosalind.info/problems/dna/
def quantidade_nucleotideo(seq):
      #return seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")
      return " ".join(map(str,[seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")]))

# Transcribing DNA into RNA - http://rosalind.info/problems/rna/
def transcrever_DNA(seq):
    return seq.replace('T', 'U')


#print(quantidade_nucleotideo("GATGGAACTTGACTACGTAAATT"))
