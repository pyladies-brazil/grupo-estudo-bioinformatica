import re
import urllib.request

# copiei o arquivo aqui por que era pequeno, em outros casos é melhor usar o open()
arquivo = '''P01190_COLI_BOVIN
Q05557
A6UUD2
P20840_SAG1_YEAST
P01589_IL2A_HUMAN
P04441_HG2A_MOUSE
Q90X23
P07204_TRBM_HUMAN
B5FNU0
P07358_CO8B_HUMAN
Q0TMT1
P14210_HGF_HUMAN
P01045_KNH2_BOVIN
P04921_GLPC_HUMAN
P02725_GLP_PIG'''

# funções
def find_motif(txt, header):
  motifs =[]
  padrao = r"N[^P][ST][^P]"
  for x in range(len(txt)-3):
    if re.match(padrao,txt[x:x+4]):
      motifs.append(str(x+1))
  if motifs!=[]:
    print(header)
    print(" ".join(motifs))

def read_seq(page,x):
  f = urllib.request.urlopen(page).readlines()
  seq =""
  for line in f:
    lin = line.decode('utf-8')
    if lin[0] == '>':
      header = lin
    else:
      seq+=lin.rstrip()
  find_motif(seq,x)

#aplicando as funções ao arquivo  
for x in arquivo.split():
  read_seq("https://www.uniprot.org/uniprot/%s.fasta" % x,x)

