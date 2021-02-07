from graphviz import Digraph

dot = Digraph(comment='rosalind overlap graph')

def graphReadFasta(file,n):
    f = open(file,"r").readlines()
    f.append('>FIM\n')

    header=''
    seq=''
    prefix =[]
    sufix =[]
        
    for line in f:
        if line[0] == '>':
            if header!='':
                prefix.append([header,seq[0:n]])
                sufix.append([header,seq[-n:]])
            header = line.rstrip()
            header = header[1:]
            seq =''
        else:
            seq += line.rstrip() 
    return prefix , sufix
    
#print(graphReadFasta("rosalind_grph1.txt",3))

def graphOverlap(prefix,sufix):
    result= [] 
    #result = "" ## para printar o resultado
    for x in range(len(sufix)):
        for i in range(len(prefix)):
            if sufix[x][0]!= prefix[i][0] and sufix[x][1] == prefix[i][1]:
                result.append((sufix[x][0],prefix[i][0])) 
                #result+= sufix[x][0] + " " + prefix[i][0] + "\n" ## para printar o resultado
    return result

a,b = graphReadFasta("rosalind_grph1.txt",3)
c = graphOverlap(a,b)
#print(graphOverlap(a,b))

for x in a:
  dot.node(x[0])

for x in c:
  dot.edge(x[0],x[1])

dot.format = 'png'
dot.view(filename='digraph', directory='./')
#print(c)

