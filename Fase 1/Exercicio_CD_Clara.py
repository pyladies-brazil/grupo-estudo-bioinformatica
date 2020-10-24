''' exercício C '''

codigoComplementarDNA = {
    'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def DNA_complemento_reverso(seq, dic):
    ''' (str, dict) -> str
    Retorna o complemento reverso de uma sequencia de DNA de acordo com um dicionário
    '''
    seqComplementar = ""
    for n in seq[::-1]:
        seqComplementar += dic[n]  
    return seqComplementar

#print(DNA_complemento_reverso("ATCGGCCGCTTT",codigoComplementarDNA))
    
''' exercício D '''

def porcentagem_CG(string):
    return 100*((string.count('C') + string.count('G'))/(float(len(string))))


def batch_CG_FASTA(arquivo):
    '''
    nota: essa versão não salva os dados,
    apenas adiciona a maior porcentagem ao chegar na próxima tag (>)
    por isso precisa colocar uma linha extra ou não conta a ultima sequencia

    '''
    f = open(arquivo,"r").readlines()
    f.append('>FIM\n')

    noobstorage = ["", 0 ]
    
    nome = None
    s = ''
    for line in f:
        line = line.rstrip()
        if line.startswith('>'):
            if len(s)>0:
                CG = porcentagem_CG(s)
                if CG>noobstorage[1]:
                    noobstorage[0]=nome
                    noobstorage[1]=CG
            nome = line            
            s = ''
        else:
            s = s + line      

    return noobstorage
    
#print(batch_CG_FASTA("rosalind_gc.txt"))
