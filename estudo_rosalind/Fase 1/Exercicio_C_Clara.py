#-----------Encontro 3-------------#
#-----Counting Point Mutations-----#

     
def contar_mutacoes_pontuais(seq1,seq2):
    num = 0
    for n,i in zip(seq1,seq2):
        if n!=i:
            num+=1
    return num
    #return sum(n!= i for n,i in zip(seq1,seq2))


#print(contar_mutacoes_pontuais("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"))
