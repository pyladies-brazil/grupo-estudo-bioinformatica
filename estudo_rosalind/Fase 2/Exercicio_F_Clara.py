### Reaproveitando código para tradução
codigoAA = {
    'ata':'I', 'atc':'I', 'att':'I', 'atg':'M', 'aca':'T', 'acc':'T',
    'acg':'T', 'act':'T', 'aac':'N', 'aat':'N', 'aaa':'K', 'aag':'K',
    'agc':'S', 'agt':'S', 'aga':'R', 'agg':'R', 'cta':'L', 'ctc':'L',
    'ctg':'L', 'ctt':'L', 'cca':'P', 'ccc':'P', 'ccg':'P', 'cct':'P',
    'cac':'H', 'cat':'H', 'caa':'Q', 'cag':'Q', 'cga':'R', 'cgc':'R',
    'cgg':'R', 'cgt':'R', 'gta':'V', 'gtc':'V', 'gtg':'V', 'gtt':'V',
    'gca':'A', 'gcc':'A', 'gcg':'A', 'gct':'A', 'gac':'D', 'gat':'D',
    'gaa':'E', 'gag':'E', 'gga':'G', 'ggc':'G', 'ggg':'G', 'ggt':'G',
    'tca':'S', 'tcc':'S', 'tcg':'S', 'tct':'S', 'ttc':'F', 'ttt':'F',
    'tta':'L', 'ttg':'L', 'tac':'Y', 'tat':'Y', 'taa':'_', 'tag':'_',
    'tgc':'C', 'tgt':'C', 'tga':'_', 'tgg':'W'}

def traducao(seq):
    '''(str) -> str
    retorna a sequencia de dna traduzida em uma proteina
    caso haja um nucleotideo nao determinado será adicionado o aminoacido "X"
    que é referencia para aminoacido nao identificado'''
    proteina = ''
    for n in range(0,len(seq),3):
        if seq[n:n+3] in codigoAA:
            proteina += codigoAA[seq[n:n+3]]
        else:
            if n+3 < len (seq):
                proteina+= 'X'
    return proteina  



### montando a lista com a sequencia e os exons
f = open('arquivo.fasta',"r").readlines()
f.append('>FIM\n')

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

### juntando tudo  
seq = seqs[0]
seqs = seqs [1:]
#print(seq, seqs)
for intron in seqs:
  seq= seq.replace(intron, '') 

#nota: a ultima letra sempre será um stop codon = "_"
print(traducao(seq.lower())[:-1])
