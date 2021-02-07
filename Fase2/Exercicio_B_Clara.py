def mortal_rabbits(n, m):
    sequence = [1, 1]
    
    for i in range(n - 2):
        new_num = 0
        if i + 2 < m:
            #Normal fibonacci - ninguem morreu ainda
            new_num = sequence[i] + sequence[i + 1]
            #print("no dead yet", sequence, new_num)
        else:
            # considerando as mortes d m gerações atrás
            #new_num = sum(sequence[-m:-1])
            # new_num vai ser a soma dos filhotes das m gerações anteriores 
            for j in range(m - 1):
               new_num += sequence[i - j]
            ##    #print("die", sequence, new_num)
        sequence.append(new_num)
    #print("ultimo", sequence, new_num)
    return sequence[-1]

mortal_rabbits(10,5)
